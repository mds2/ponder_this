Problem
=======

This month's challenge is in honor of the late Professor Solomon Golomb (https://en.wikipedia.org/wiki/Solomon_W._Golomb), who received the National Medal of Science from President Obama on February 2, 2013. Prof. Golomb received his award in the same ceremony as Rangaswamy Srinivasan from IBM, who was awarded his medal for contributions to laser eye surgery. 
Golomb proved that any 2^Nx2^N board with a missing square can be tiled with a single r-shaped tromino. 
Find at most three types of pentominos (http://mathworld.wolfram.com/Pentomino.html) that can tile every 4^Nx4^N board with a missing square. 
Prove your solution.


Solution
================

Strategy
-----------

Analogously to a possible proof of the Golomb tromino theorem (and without looking at the Befumo and Lenchner paper that comes up when I search for the actual Golomb tromino theorem -- hopefully the details of mine will be different from that one) we will adopt a recursive solution.

Namely we will first show that 2 free pentominoes are sufficient to tile a 4x4 checkerboard with any one square missing.

Then we will proceed to use those exact same pentominoes to completely tile 4x enlarged copies of themselves.

We will proceed to show that these same pentominoes can tile any `4^n x 4^n` square using the inductive argument that naturally falls out of these constructions.

Pentominoes used
---------------

First pentomino shape

    x x
    x
    x
    x

Second pentomino shape

    x x
    x x
    x

Tilings of a 4x4 board
--------------------

With a corner missing

    1 1 2 2
    1 1 2 2
    1 3 3 2
    3 3 3

With rotations, we can align the missing corner square with any corner

With an edge square missing

    1 1 2 2
    1 3 3 2
    1 3 3 2
    1 3   2

With rotations and reflections, we can align the missing edge square with
any non-corner edge square.

With one of the 4 squares missing which are not on any edge

    1 1 2 2
    1 3   2
    1 3 3 2
    1 3 3 2

With rotations, this can match any of the 4 squares that are not on any edge.


Construction of rep-tiles
-----------------

To make 4x scaled copies of our tiles out of our tiles we will
first construct a series of roughly 4x4 blocks with some squares missing,
and some squares outside the 4x4 square defining the block.

In general, each of these blocks will have `n` missing squres within the
4x4 region defining them, and `n-1` extra squares outside of their
4x4 block.

block 1 is just a 4x4 block with a corner piece missing

    1 1 2 2
    1 1 2 2
    1 3 3 2
    3 3 3 .

block 2 overhangs by one square, and has two internal missing squares.

    1
    1 1 3 3
    1 1 3 3
    2 2 2 3
    2 2 . .

block 3 overhangs by 2 squares, and has 3 internal missing squares

    1
    1
    1 2 2 2
    1 1 2 2
    3 3 3 3
    3 . . .

blocks 4 and 6 each overhang by 3 squares and have 4 internal missing squraes

block 4

    1
    1
    1
    1 1 2 2
    3 3 2 2
    3 3 3 2
    . . . .

block 6

    1 1 1
    1 1 2 2
    3 3 2 2
    3 3 3 2
    . . . .

block 5, by our scheme, would have 5 internal missing squares, but we will
fill these with an extr tile, to yield a 5x4 completely filled block

    1 1 2 2
    1 1 2 2
    1 3 4 2
    3 3 4 4
    3 3 4 4

To compose our larger pieces out of our blocks, we can do the following


    2 1
    3 4 5

and

    1
    2 3 6 5

Drawn out, these shapes look like


    5 5 4 4 4 1 1 1
    5 5 4 4 2 2 1 1
    7 5 6 6 2 2 3 3
    7 6 6 6 2 3 3 3
    7 8 8 8 A A A D D D E E
    7 7 8 8 A A B D D E E E
    9 9 9 9 C B B F F G G G
    9 C C C C B B F F F G G


and

    5 5 4 4 4 1 1 1
    5 5 4 4 2 2 1 1
    7 5 6 6 2 2 3 3
    7 6 6 6 2 3 3 3
    7 8 8 8
    7 7 8 8
    9 9 9 9
    9 A A A
    B B A A
    B B C C
    B C C C
    D D E E
    D D E E
    D F G E
    F F G G
    F F G G


Final proof
------------

To show that our choice of pentominoes can fill any `4^n x 4^n` board with
any arbitrary one square missing, we will induct on `n`.

For our base case, recall our tilings of a `4x4` board with one tile missing
using our selection of pentominoes.

Now on to our inductive step.

Given our construction that allows us to generate copies of our tiles
scaled up by a factor of 4 in each dimension from unscaled copies of our tiles,
we can, by an inductive argument that we omit here, make `4^m x 4^m`
copies of each of our tiles for any `m`

To fill a `4^n x 4^n` board with one square missing, first we make
copies of our tiles scaled by `4^(n-1)` in each dimension.

Then we subdivide our board into non-overlapping squares of size `4^(n-1)`.
We make note of which of these non-overlapping squares contains the square
to be left missing.

Then, using our tiles that have been scaled up by
`4^(n-1)` in each dimension,
fill all of our board except for the `4^(n-1) x 4^(n-1)` subsquare
containing the missing square.

The subsquare containing the missing square is now empty, and is, thus
a smaller version of our original problem.  Induct accordingly.

    
