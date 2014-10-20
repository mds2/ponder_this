
Solution?
=====

First, we simplify notation to avoid writing `2^(3^(4^(5^(6^(7^(8^9))))))`

Define `wow(i,j)` (rhymes with `pow(i,j)`) as follows.

 * `wow(i,i) = i`
 * `wow(i,j) = i ^ (wow(i + 1, j))` for `j > i`

We are concerned with `wow(2,9) mod (10 ^ 10)`

First steps
-------

Consider `wow (2, 9) mod (10 ^ 10)` which is
`(2 ^ wow(3, 9)) mod (10 ^ 10)`

We can represent that as
`(2 ^ 10) * [(2 ^ (wow (3,9) - 10)) mod (5 ^ 10)]`
which is

Because `2` is relatively coprime to `5`, `2^X mod (5 ^ 10)`
must cycle every `(5 ^ 9) * 4` times `X` is incremented. 

So now we need to find

`wow (3,9) mod (4 * (5 ^ 9))`

`3` is relatively coprime to both `2` and `5` so this is

`3 ^ [wow (4, 9) mod (2 * 4 * (5 ^ 8))]`

Now we must find `wow (4, 9) mod (2 * 4 * (5 ^ 8))`
which is
`4 * 4 * [4 ^ (wow (5, 9) - 2) ] mod (2 * 4 * (5 ^ 8))`
or 
`8 * [(2 * 4 ^ (wow (5, 9) - 2) mod (5 ^ 8)) ] mod (2 * 4 * (5 ^ 8))`
or 
`8 * [2 * 4 ^ ([wow (5, 9) mod (4 * 5 ^ 7)] - 2) ] mod (2 * 4 * (5 ^ 8))`

So now we need

`wow (5, 9) mod (4 * 5 ^ 7)`

which is

`(5 ^ 7) * [(5 ^ (wow (6, 9) - 7)) mod 4]`

but since `5 mod 4 == 1`

this is `wow (5, 9) mod (4 * 5 ^ 7) == (5 ^ 7) == 78125`

so
`wow (4, 9) mod (2 * 4 * (5 ^ 8)) == 8 * (2 * 4 ^ (5 ^ 7 - 2)) mod (2 * 4 * (5 ^ 8))`
or
`390624`

and 
`wow (3,9) mod (4 * (5 ^ 9))`
is
`3 ^ [wow (4, 9) mod (2 * 4 * (5 ^ 8))] mod (4 * 5 ^ 9)`
`3 ^ [390624] mod (4 * 5 ^ 9)`
or
`5765981`

and `wow (2,9) mod (10 ^ 10)` is
`(2 ^ 10) * [(2 ^ (wow (3,9) - 10)) mod (5 ^ 10)]`
or
`(2 ^ 10) * [(2 ^ (5765981 - 10)) mod (5 ^ 10)]`

The last part gives us

    user=> (mod (pow 2 (- 5765981 10)) (pow 5 10))
    7978848

from which we get

    user=> (mod (* 7978848 (pow 2 10)) (pow 10 10))
    8170340352
