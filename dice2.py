#!/usr/bin/env python3
# (c) Patrick de Kok 2014
import random
import re

def roll(dice_expr):
    return dice_expr.__roll__()


def E(dice_expr):
    return dice_expr.__expectancy__()


class Constant:
    def __init__(self, value):
        self._value = value

    def __max__(self):
        return self._value

    def __min__(self):
        return self._value

    def __str__(self):
        return str(self._value)

    def __roll__(self):
        return self._value

    def __expectancy__(self):
        return self._value

    def __repr__(self):
        return "dice.Constant({})".format(self._value)


class Dice:
    def __init__(self, expression):
        """
        Transform the string expression into some internal representation.
        The internal representation has a templated string and an iterable
        of abstract syntax trees.
        """
        self._template, self._asts = __parse_dice_expression(expression)
        pass

    def __max__(self):
        """Return an iterable of the maximum values of each AST."""
        return (max(d) for d in self._asts)

    def __min__(self):
        """Return an iterable of the minimum values of each AST."""
        return (min(d) for d in self._asts)

    def __str__(self):
        return self._template % roll(self)

    def __roll__(self):
        """Return an iterable of random values generated by each AST."""
        return (d.roll() for d in self._asts)

    def __expectancy__(self):
        """Return an iterable of expectancy values of each AST."""
        pass

    def __repr__(self):
        return self._template % [str(ast) for ast in self._asts]
