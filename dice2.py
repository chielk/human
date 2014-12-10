#!/usr/bin/env python3
# (c) Patrick de Kok 2014
import random
import re


def roll(dice_expr):
    """
    Operator to evaluate DiceExpressions to its random value.

    Unparsed strings can be passed as well.
    """
    return dice_expr.__roll__()


def E(dice_expr):
    """
    Operator to evaluate DiceExpressions to its expectancy.

    Unparsed strings can be passed as well.
    """
    return dice_expr.__expectancy__()


class Element:
    def __init__(self, number):
        number = re.sub(" ", "", number)
        self._number = int(number)

    def __max__(self):
        return self._number

    def __min__(self):
        return self._number

    def __str__(self):
        return str(self._number)

    def __roll__(self):
        return self._number

    def __expectancy__(self):
        return self._number

    def __repr__(self):
        return 'dice.Element("{}")'.format(self._number)


class Dice(Element):
    def __init__(self, expression):
        pattern = re.compile("(?P<sign>[+-]?) *(?P<number>\d*)d(?P<sides>\d+)")
        dice = pattern.match(expression).groupdict()

        self._sign = -1 if dice["sign"] == "-" else 1
        self._sides = int(dice["sides"])
        number = dice["number"] if dice["number"] else "1"
        super().__init__(number)

    def __roll_die(self):
        """Roll a single die."""
        return random.randint(1, self._sides)

    def __max__(self):
        return self._sign * self._number * self._sides

    def __min__(self):
        return self._sign * self._number

    def __str__(self):
        s = "-" if self._sign == -1 else ""
        return s + "{}d{}".format(self._number, self._sides)

    def __roll__(self):
        return (self._sign *
                sum((self.__roll_die() for _ in range(self._number))))

    def __expectancy__(self):
        expectancy = self._number * (self._sides + 1) / 2
        if expectancy.is_integer():
            expectancy = int(expectancy)  # Omit floating point
        return self._sign * expectancy

    def __repr__(self):
        return 'dice.Dice("{}")'.format(self.__str__())


class DiceExpression:
    def __init__(self, expression):
        """
        Transform the string expression into some internal representation.
        The internal representation has a templated string and an iterable
        of abstract syntax trees.
        """
        self._template, self._asts = self.__parse_expression(expression)

    def __max__(self):
        """Return an iterable of the maximum values of each AST."""
        return (max(d) for d in self._asts)

    def __min__(self):
        """Return an iterable of the minimum values of each AST."""
        return (min(d) for d in self._asts)

    def __str__(self):
        return self._template.format(roll(self))

    def __roll__(self):
        """Return an iterable of random values generated by each AST."""
        return (roll(d) for d in self._asts)

    def roll(self):
        return sum(self.__roll__())

    def E(self):
        """Return an iterable of expectancy values of each AST."""
        return sum(d.__expectancy__() for d in self._asts)

    def __repr__(self):
        return self._template.format(str(ast) for ast in self._asts)

    def __parse_expression(self, expression):
        pattern = re.compile("([+-]? *\d*d?\d+)")
        template = pattern.sub("{}", expression)
        asts = []
        for substring in pattern.findall(expression):
            if "d" in substring:
                asts.append(Dice(substring))
            else:
                asts.append(Element(substring))

        return template, asts

