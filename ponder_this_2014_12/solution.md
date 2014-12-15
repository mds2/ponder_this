
Solution
=====

Problem statement
----

Given an NxM binary matrix, we can compute the N sums of the rows and the M sums of the columns . These sums can sometimes uniquely define the matrix. For example, the sums `[1,2,0][2,1]` can be generated only from the matrix


    1 0
    1 1
    0 0


But sometimes there are several options. For example [1,1,2][2,2] can be generated from two matrices:

    0 1    1 0
    1 0    0 1
    1 1    1 1

The challenge this month is to find sums that are generated from exactly 29 different binary matrices.

To rule out trivial solution, we further require that each matrix have no more than 50 bits.

Please provide your answer as two lines, the first line with N integers and the second with M integers. N*M should be no more than 50.

Short answers
-----

Either one of the following work.

Solution 1
 
    7 7 7 7 1 
    4 4 4 4 4 4 4 1
 
Solution 2
 
    14 14 1
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 1

Explanation
-----

For any `m` and `n`, one can create sums of dimensions `(m+1) ` and  `(n+1)`
which are satisfied by exactly `m*n + 1` binary matrices (of size `(m+1) x (n+1)`).

This is done by setting each of the `m` leftmost columns to have a sum of `n`,
setting the rightmost column to have a sum of `1`, setting the `n` topmost rows to
each have a sum of `m`, and setting the bottom row to have a sum of `1`.

There are `(n*m) + 1` ways to satisfy this set of sums.

The first `n*m` ways are found by forcing the bottom right entry of the matrix to be
zero.  Because the sums of the bottom row and the left column must be 1, there must be
exactly one `1` in each of these.  These `1`s uniquely determine which entry in the upper left `n*m` entries must be `0` for each of the remaining rows to have sum `m`
and each of the remaining columns to have sum `n`.  There are `n*m` ways to
pick where to place a `1` in both the leftmost `m` entries of the bottom row
and the top `n` entries of the rightmost column (alternatively exactly `n*m`
ways to pick the unique `0` entry in the upper left `n x m` submatrix).

The remaining `1` way is found by forcing the bottom right entry of the matrix
to be a `1` and recognizing that this forces the values of the entries in the rest
of the matrix.
