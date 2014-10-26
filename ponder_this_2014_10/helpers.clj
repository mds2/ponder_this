;;; Originally this started as a collection of helper functions for the work
;;; performed in `solution.md` -- but eventually it became a full-fledged
;;; solver for this particular puzzle, in the form of the function `solve-it`

(defn factor
  {:doc "\"factor\" factors its single argument"
   :test (fn []
           (let [result (factor 42)]
             (assert (= (apply * result) 42))
             (assert (= (count result) 3))))}
  [n]
  (if (< n 2) []
      (if (= (mod n 2) 0)
        (conj (factor (/ n 2)) 2)
        (if (= (mod n 3) 0)
          (conj (factor (/ n 3)) 3)
          (if (= (mod n 5) 0)
            (conj (factor (/ n 5)) 5)
            (loop [guess 6]
              (if (= (mod n (+ guess 1)) 0)
                (conj (factor (/ n (+ guess 1))) (+ guess 1))
                (if (= (mod n (+ guess 5)) 0)
                  (conj (factor (/ n (+ guess 5))) (+ guess 5))
                  (if (> (* guess guess) n)
                    (conj [] n)
                    (recur (+ guess 6)))))))))))

(defn count-factors
  {:doc "takes the output of \"factor\" and transforms it into a list of
  pairs such that the first item of every pair is a prime, and the
  second item is the multiplicity of that prime in the input list
  \"factors\"" }
  [factors]
  (loop [return-value '() remaining factors]
    (if (empty? remaining) return-value
        (let [factor (first remaining)]
          (recur (conj return-value [factor, (count (filter #(= % factor)
                                                            remaining))])
                 (filter #(not (= % factor)) remaining))))))

(defn pow
  {:doc "Raises a to the power of b" }
  [a b]
  (loop [accum 1 factors-left b base a]
    (if (< factors-left 1) accum
        (if (= (mod factors-left 2) 1)
          (recur (* accum base) (/ (- factors-left 1) 2) (* base base))
          (recur accum (/ factors-left 2) (* base base))))))

(defn gcd [a b]
  (if (= a 0) b
      (if (= b 0) a
          (recur (mod b a) a))))

(defn mul-factors
  {:doc "Turns the output of \"count-factors\" into a product.
  '([3 2] [5 1]) becomes (* (pow 3 2) (pow 5 1))." }
  [factor-pairs]
  (reduce (fn [x y] (* (pow (nth y 0) (nth y 1)) x)) 1 factor-pairs))

(defn get-next-mod-by
  {:doc "Core trick of the puzzle. (mod (pow a b) m) is equal to (mod (pow a
  (mod b (get-next-mod-by m))) m)"}
  [old-mod]
  (loop [pairs-out '() pairs-left (count-factors (factor old-mod))]
    (if (empty? pairs-left) (mul-factors pairs-out)
        (let [pair (first pairs-left) remaining-pairs (rest pairs-left)]
          (recur (conj pairs-out
                       [(- (nth pair 0) 1) 1]
                       [(nth pair 0) (- (nth pair 1) 1)])
                 remaining-pairs)))))

(defn solve-it
  {:doc "Computes [base ^ ((base + 1) ^ ... ^ max-exp)]  modulo mod-by"}
  [base max-exp mod-by]
  (println "Recursing with args " (str (list base max-exp mod-by)))
  (if (= max-exp base) (mod base mod-by)
      (if (= (gcd mod-by base) mod-by) 0
          (if (= (mod base mod-by) 1) 1
              (loop [accum 1 offset-exp 0 mod-by-with-factors-removed mod-by]
                (if (= (mod mod-by-with-factors-removed base) 0)
                ;;; we remove a factor from mod-by-with-factors-removed
                ;;; and adjust offset-exp
                  (recur (* base accum) (+ offset-exp 1)
                         (/ mod-by-with-factors-removed base))
                ;;; otherwise we make the final call
                  (let [next-mod-by (get-next-mod-by
                                     mod-by-with-factors-removed)]
                    (mod (* accum
                            (pow base
                                 (mod
                                  (-
                                   (solve-it (+ base 1) max-exp
                                             next-mod-by)
                                   offset-exp) next-mod-by)))
                         mod-by)
              )))))))

      
