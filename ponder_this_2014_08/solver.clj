
(defn min-cost [num-items]
  (loop [n 2
         prev-answers [0 0] ]
    (if (> n num-items)
      prev-answers
      (recur
       (+ n 1)
       (conj prev-answers
             (apply min (map (fn [choice]
                               (+ (* choice 10) (- n choice)
                                  (nth prev-answers choice)
                                  (nth prev-answers (- n choice))
                                  )
                               )
                             (range 1 n))
                    )
             )
       ))))

(defn print-answers [num-items]
  (loop [i 0 answers (min-cost num-items)]
    (if (and (> i 0) (not (empty? answers)))
      (println "Cost to solve for " (str i) " integers is "
               (str (/ (first answers) i)))
      )
    (if (empty? answers)
      "done"
      (recur (+ i 1) (rest answers))
      )
    )
  )


