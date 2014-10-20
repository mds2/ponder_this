
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

(defn get-choices [num-items]
  (let [costs (min-cost num-items)]
    (map (fn [i] (filter (fn [choice]
                           (= (+ (* choice 10) (- i choice)
                                 (nth costs choice)
                                 (nth costs (- i choice)))
                              (nth costs i)))
                         (range i)))
         (range (+ num-items 1)))
    ))

(defn get-tree-depths [num-items]
  (let [choices (map #(first (reverse (cons 0 %))) (get-choices num-items))]
    (map (fn [n]
           (loop [low 1 high num-items mid (+ 1 (nth choices num-items)) count 0]
             (if (= mid n) count
                 (if (> mid n)
                   (recur low (- mid 1)
                          (+ low (nth choices (- mid low) )) (+ count 1))
                   (recur mid high (+ mid (nth choices (+ (- high mid) 1) ))
                          (+ count 1))
                   ))))
         (range 1 (+ num-items 1)))
    ))



(defn print-tree [num-items]
  (let [depths (get-tree-depths num-items)]
    (loop [level 0 remaining (apply max depths)]
      (if (< remaining 1)
        (println "done")
        (do
          (println (apply str (map (fn [i] (if (= (nth depths i) level) "*"
                                               (if (< (nth depths i) level)
                                                 "|" " ")))
                                   (range num-items))))
          (recur (+ level 1) (- remaining 1)))
        ))))
