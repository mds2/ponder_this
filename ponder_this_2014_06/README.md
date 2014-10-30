Reasoning
=======

Rather than use the projective geometry approach outlined in the official solution, 
I proceeded (slightly hackily, but still provably, as I wrote a verifier) by reasoning about cliques in graphs.

I treated each cube as a node in a larger graph, and considered two cubes to be
connected if they shared a number.

Further I use the numbering to partition the edges of the resulting graph into
at most 31 cliques.

The constraint that each cube have 6 different numbers requires that each cube be a
member of exactly 6 of these cliques.

The constraint that any two cubes share exactly one common number means that
 * No two cliques share an edge
 * The union of all the edges in all the cliques forms the complete graph on 25 nodes.

Relationships between clique sizes
--------

Here is where I started to get a foothold on the problem.

The complete graph on 25 vertices contains `25 * 24` or `5 * 5 * 6 * 4` edges.

If each clique is of size 5, there are `5 * 4` edges per clique.

Each cube is a member of exactly 6 cliques, each clique has `5` members, one of which
is the current cube.  So each cube has `4` neighbors other than itself in each of the `6` cliques of which it is a member and has `24` neighbors other than itself in the complete graph on `25` nodes.  `6 * 4 = 24`.

If such a partition of `K_{25}` were possible, how many cliques would that give us total?

If we multiply each node by the number of cliques of which it is a member, we overcount
by a factor of the size of each clique (since each clique is the same size).

That gives us `25 * 6 / 5 = 5 * 6 = 30` cliques.

So now we try to partition `K_25` into 30 non-overlapping cliques of size `5` such that each node is in exactly `6` cliques.

Buidling our partition
-------
