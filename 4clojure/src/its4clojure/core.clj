(ns its4clojure.core)

(defn pascal
  [n]
  (if (= 1 n)
    [1]
    (concat
      [1]
      (map + (pascal (dec n)) (next (pascal (dec n))))
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

(defn my-map
  [f coll]
  (if-let [h (first coll)]
    (lazy-seq
      (cons (f h) (my-map f (next coll))))))

(defn lcm
  [a b & more]
  (let [bs (iterate #(+ b %) b)
        n (some #(when (zero? (mod % a)) %) bs)]
    (if more
      (apply lcm n more)
      n)))

(defn un-interleave
  [coll n])