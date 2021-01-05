(ns its4clojure.core)

(defn fibonacci
  [n]
  (if (= 1 n)
    [1]
    (concat
      [1]
      (map + (fibonacci (dec n)) (next (fibonacci (dec n))))
      [1])))


(defn my-flatten
  "Re-implement flatten"
  [xs]
  (if-not (coll? xs)
    xs
    (reduce
      (fn [a x]
        (if (coll? x)
          (into a (map my-flatten x))
          (conj a x)))
      []
      xs)))


