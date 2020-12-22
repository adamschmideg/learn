(ns hackerrank.core)

(defn evens-odds
  [s]
  (let [counts (vals (frequencies s))
        evens (->> counts
                  (map #(quot % 2))
                  (remove zero?))
        odds (->> counts
                  (map #(mod % 2))
                  (remove zero?))]
    [evens odds]))

(defn max-palindrome-length
  [s]
  (let [[evens odds] (evens-odds s)
        total (* 2 (apply + evens))]
    (if (seq odds) (inc total) total)))

(defn maximum-palindromes
  ([s]
   (let [[evens odds] (evens-odds s)
         total-odds (apply + odds)
         total-odds (if (zero? total-odds) 1 total-odds)
         fact (fn [n] (reduce * (range 1 (inc n))))
         counter (fact (apply + evens))
         divisor (apply * (map fact evens))]
     (* total-odds (/ counter divisor))))

  ([s begin end] (maximum-palindromes (subs s (dec begin) end))))

