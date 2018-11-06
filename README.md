# Simplex

A Implementation of Simplex Algorithm using Python

## Definition

This project will receive a file with a well defined structure, as:

```
Line 1: The z to maximize
Line 2: Constraint 1
Line 3: Constraint 2
Line n: Constraint n
Line n+1: End of file indication ("-")
```

For the following model:

```
z = 8x1 + 12x2

20x1 + 60x2 <= 60000
70x1 + 60x2 <= 84000
12x1 + 4x2 <= 14400

```

We have to write the following file:

```
8 12
20 60 60000
70 60 84000
12 4 14400
-
```

The result for the model will be:

```
480 840 13920
```

Representing:

```
z = 13920
x1 = 480
x2 = 840
```

## Executing

There are some examples in the dir "input":

```
$ python simplex.py < input/a.input
```
