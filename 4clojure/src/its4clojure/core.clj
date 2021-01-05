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

(defmacro dbg [body]
  `(let [x# ~body]
     (println "dbg:" '~body "=" x#)
     x#))

(defn btree?
  [x]
  (or
    (nil? x)
    (and
      (coll? x)
      (= 3 (count x))
      (btree? (fnext x))
      (btree? (last x)))))


(println (btree? [1 2 3 4]))