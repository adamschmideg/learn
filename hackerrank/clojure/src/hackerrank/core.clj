(ns hackerrank.core)

(defn max-palindrome-length
  [s]
  (let [counts (vals (frequencies s))
        pairs (apply + (map #(quot % 2) counts))
        odds? (some #(= 1 (mod % 2)) counts)
        evens (* 2 pairs)]
    (if odds? (inc evens) evens)))

(defn maximum-palindromes
  ([s] s)
  ([s begin end] (maximum-palindromes (subs s (dec begin) end))))

