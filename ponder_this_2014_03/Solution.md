IBM Research "Ponder This" March 2014
=================

Problem statement
----------------------

N lamps are set in a circle, and for each integer M you have a tool that can toggle the state (on/off) of any set of M consecutive lamps. 
Find a possible N which satisfies the following statements:

 * The sum of its digits is less than 10.
 * By applying the tool for M=105 several times, we can toggle a single lamp.
 * If we remove one lamp and start from a random initial setting for the remaining N-1 lamps, the probability that there exists a way to apply the tool for M=32 several times and switch all the lamps off is less than 0.001%.
 
Short answer
----

Solutions include

 `1121`, `1601`, and `2113`

Characteristics of solutions when the "sum of digits" constraint is relaxed
-----

*Any number, `n`, relatively coprime to `105` satsifies constraint 2 if `(105 * k - 1) / n` is even, where `k` is the multiplicative inverse of `105` modulo `n`
---

If the number of lamps is coprime to `105` (and, presumably, larger than `105`, although allowing fewer lamps allows for interesting trivial solutions, such as `32`), one can proceed to toggle an individual lamp as follows.

 * Starting with the lamp we wish to toggle, toggle `105` lamps (going clockwise)
 * Starting with the lamp just after the most clockwise lamp we toggled, toggle `105` lamps.
 * Stop when the last lamp we toggled is the one we set out to toggle.
 * Because `(105 * k - 1) / n` is even, we must have toggled every lamp except the last one an even number of times.  We toggled the last one an odd number of times.

Any `n` such that `n-1` is a multiple of `32` satisfies constraint 3
-------

Imagine a circulant matrix over integers modulo `2` each of whose columns contain `32` consecutive `1`s and the rest of the entries as `0`.

Toggling `32` consecutive lamps is like picking `1` lamp, making the indicator vector for that lamp, and then multiplying it by the above circulant matrix.

Such a matrix has a nullspace of dimension at least `31`, for the following reason.

For any `0 < i < 32` the vector which is `1` in any position which is `i` or `0` modulo `32` and `0` everywhere else maps to the null vector.

This means that the probability of being able to switch all the lamps off is equal to the probability that the coefficients of all basis vectors not in the span of the above circulant matrix are all zero.  This is at most `1 / (2 ^ 31) ` as there are 31 independent vectors in the null space of the matrix.

One can equivalently use the pidgeonhold principle with the above null-space construction to show that, for any arrangement of lamps that can be turned off, there are `2 ^ (31) - 1` distinct sets of places at which to apply "the tool" that will toggle the same set of lights.

A similar result can be obtained by noting that along any set of lights spaced by intervals of 16 (with a total number of lights which is a multiple of 32), the parity of the sum of the states of the lights in the set must remain unchanted by any toggling of 32 contiguous (adjacent) lights.  There are 16 non-overlapping sets of this sort, and each has a probability `1/2` of having a parity of `0`.  Alternatively one can use the nullspace vectors mentioned above with a similar parity constraint.

We can find these easily in ruby
-----

Consider

`1.upto(100).find_all{|i| ((32 * i) + 1).digits.reduce{|x,y|x+y} < 10 and ((32 * i) + 1).gcd(105) == 1}` where `digits` and `gcd` are defined below

    class Fixnum
      def factor
        result = []
        remaining = self
        try_to_divide_by = 2
        while remaining > 1
          while (remaining % try_to_divide_by) == 0
            result << try_to_divide_by
            remaining = remaining / try_to_divide_by
          end
          try_to_divide_by += 1
        end
        return result
      end

      def gcd(b)
        if b == 0
          return self
        end
        return b.gcd(self % b)
      end

      def orbit_modulo(n)
        return 0.upto(n).map{|i| (self * i) % n}
      end

      def inverses_modulo(n)
        return 0.upto(n).find_all{ |i| ((self * i) % n) == 1}
      end

      def digits
        remaining = self
        result = []
        while remaining > 0
          result << (remaining % 10)
          remaining = remaining / 10
        end
        return result
      end
    end



The results of the computation ` 1.upto(100).find_all{|i| ((32 * i) + 1).digits.reduce{|x,y|x+y} < 10 and ((32 * i) + 1).gcd(105) == 1}` are 
`[0, 35, 41, 50, 66, 95]`

Now we will find the ones that satisfy the following

`n`, relatively coprime to `105` satsifies constraint 2 if `(105 * k - 1) / n` is even, where `k` is the multiplicative inverse of `105` modulo `n`

The following ruby computation

` 1.upto(100).find_all{|i| ((32 * i) + 1).digits.reduce{|x,y|x+y} < 10 and ((32 * i) + 1).gcd(105) == 1}.map{|i| 32 * i + 1}.map{|i| [i,105.inverses_modulo(i)]}.find_all{|l| ((105 * l[1][0] - 1) / l[0]).even?}`

finds all 

` [[1121, [363]], [1601, [61]], [2113, [161]]]`

where the first number in each pair is the number of lamps, and the second number (actually a list containing one number) is the multiplicative inverse of 105 modulo the number of lamps.

For clarity we can break it up as


    1.9.3-p125 :126 > null_space_candidates = 1.upto(106).map{|i| 32 * i + 1}
     => [33, 65, 97, 129, 161, 193, 225, 257, 289, 321, 353, 385, 417, 449, 481, 513, 545, 577, 609, 641, 673, 705, 737, 769, 801, 833, 865, 897, 929, 961, 993, 1025, 1057, 1089, 1121, 1153, 1185, 1217, 1249, 1281, 1313, 1345, 1377, 1409, 1441, 1473, 1505, 1537, 1569, 1601, 1633, 1665, 1697, 1729, 1761, 1793, 1825, 1857, 1889, 1921, 1953, 1985, 2017, 2049, 2081, 2113, 2145, 2177, 2209, 2241, 2273, 2305, 2337, 2369, 2401, 2433, 2465, 2497, 2529, 2561, 2593, 2625, 2657, 2689, 2721, 2753, 2785, 2817, 2849, 2881, 2913, 2945, 2977, 3009, 3041, 3073, 3105, 3137, 3169, 3201, 3233, 3265, 3297, 3329, 3361, 3393]
    1.9.3-p125 :127 > digits_less_than_10 = null_space_candidates.find_all{ |i| i.digits.reduce{ |x,y| x + y} < 10}
     => [33, 161, 225, 321, 513, 801, 1025, 1121, 1313, 1601, 2113, 2241, 2401, 3041, 3105, 3201]
    1.9.3-p125 :128 > coprime_with_105 = digits_less_than_10.find_all{|i| i.gcd(105) == 1}
     => [1121, 1313, 1601, 2113, 3041]
    1.9.3-p125 :129 > lamps_with_divisors = coprime_with_105.map{|i| [i, 105.inverses_modulo(i)]}
    => [[1121, [363]], [1313, [1288]], [1601, [61]], [2113, [161]], [3041, [2288]]]
    1.9.3-p125 :130 > loop_an_even_number_of_times = lamps_with_divisors.find_all{ |pair| ((pair[1][0] * 105 - 1) / pair[0]).even?}
     => [[1121, [363]], [1601, [61]], [2113, [161]]]


giving us `1121` lamps, where `(363 * 105 - 1) / 1121 == 34`, so applying the tool for `M=105` for `363` times loops around the `1121` lamps `34` times before toggling the intended lamp. `1121 - 1 == 1120 = 35 * 32`

also giving us `1601` lamps, where `(61 * 105 - 1) / 1601 == 4`, so applying the tool for `M=105` for `61` times loops around the `1601` lamps `4` times before toggling the intended lamp. `1601 - 1 == 1600 = 50 * 32`

also giving us `2113` lamps, where `(161 * 105 - 1) / 2113 == 8`, so applying the tool for `M=105` for `161` times loops around the `2113` lamps `8` times before toggling the intended lamp. `2113 - 1 == 2112 = 66 * 32`

It is likely that there are many more solutions beyond these ones.
