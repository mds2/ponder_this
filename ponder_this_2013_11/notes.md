Notes
=======

Dump of data
------

 * There are 32 1-faces in a 4-cube
 * There are 32 0-faces in a 5-cube
 * There are 32 15-faces in a 16-cube
 * There are at least 3 d-cubes with 32 k-faces

 * There are 80 1-faces in a 5-cube
 * There are 80 2-faces in a 5-cube
 * There are 80 39-faces in a 40-cube
 * There are at least 3 d-cubes with 80 k-faces

 * There are 448 1-faces in a 7-cube
 * There are 448 5-faces in a 8-cube
 * There are 448 223-faces in a 224-cube
 * There are at least 3 d-cubes with 448 k-faces

 * There are 672 2-faces in a 7-cube
 * There are 672 6-faces in a 9-cube
 * There are 672 335-faces in a 336-cube
 * There are at least 3 d-cubes with 672 k-faces

 * There are 1024 1-faces in a 8-cube
 * There are 1024 0-faces in a 10-cube
 * There are 1024 511-faces in a 512-cube
 * There are at least 3 d-cubes with 1024 k-faces

 * There are 1792 2-faces in a 8-cube
 * There are 1792 3-faces in a 8-cube
 * There are 1792 895-faces in a 896-cube
 * There are at least 3 d-cubes with 1792 k-faces

Basic formula
===

number of k-faces on a d-cube

f(k,d) == (d choose k) 2 ^ (d - k)

or

[2 ^ (d - k)] * d! / (k ! (d - k) !)

Ways to get equal numbers of sides
=======

The lateral move : keep d the same, increase k by one
---

changes by

(d-k) / [2 * (k + 1)]

so

d - k = 2*k + 2

d = 3*k + 2

k=0, d=2

a 2-cube (square) has 4 points and 4 edges.

k=1, d = 5

 * There are 80 1-faces in a 5-cube
 * There are 80 2-faces in a 5-cube

k=2, d=8

 * There are 1792 2-faces in a 8-cube
 * There are 1792 3-faces in a 8-cube


Increase d by 1, increase k by 1
---

[2 ^ (d - k)] * d! / (k ! (d - k) !)
 
vs.

[2 ^ (d - k)] * (d + 1)! / ((k + 1) ! (d - k) !)
 
change by (d + 1) / (k + 1)

Not viable.

Increase d by 1, decrease k by 1
---

[2 ^ (d - k)] * d! / (k ! (d - k) !)

vs.

[2 ^ (d + 2 - k)] * (d + 1)! / ((k - 1) ! (d + 2 - k) !)

change by

4 * (d+1) * k / [(d + 1 - k) * (d + 2 - k)]
