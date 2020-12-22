(ns hackerrank.core)

(defn evens-odds
  [s]
  (let [counts (vals (frequencies s))
        evens (->> counts
                  (map #(* 2 (quot % 2)))
                  (remove zero?))
        odds (->> counts
                  (map #(mod % 2))
                  (remove zero?))]
    [evens odds]))

(defn max-palindrome-length
  [s]
  (let [[evens odds] (evens-odds s)
        total (apply + evens)]
    (if (seq odds) (inc total) total)))

(defn maximum-palindromes
  ([s] s)
  ([s begin end] (maximum-palindromes (subs s (dec begin) end))))

