human
=====
Generate a D&D human.

Summary
-------
Generate a random human with height, weight according to D&D, hair and eye
colour, and a personality based on the Big Five personality traits.
The alignment of the human is based on its personality traits with a random
component.
Command-line arguments can force some aspects of the person.

Usage
-----
```
human.py [-h] [-m] [-f] [-t] [-s] [-b] [-l] [-n NAME] [alignment]
```
Positional arguments:
```
  alignment             Lawfulness and goodness: [LNC][GNE]
```

Optional arguments:
```
  -h, --help            show this help message and exit
  -m, --male            Make a male human
  -f, --female          Make a female human
  -t, --tall            Make a tall human
  -s, --short           Make a short human
  -b, --heavy           Make a heavy human
  -l, --light           Make a light human
  -n NAME, --name NAME  Character name
```

Installation
------------
To run this program, you need to have python version 3 installed.
To install, run:
```
sudo ./setup.py install
```
