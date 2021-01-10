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

(defn max-index
  "Return the index of the maximum element"
  [coll]
  (->> coll (map-indexed #(vector %2 %1)) sort reverse first second))

(defn split-at-less
  "Return [`ascending` `rest`] where (< (first rest) (last ascending))"
  [coll]
  (let [n (->> (map compare (next coll) coll)
               (take-while (complement neg?))
               count
               inc)]
    (split-at n coll)))


(defn biggest-is-greater
  [w]
  (let [coll (-> w seq reverse)
        [asc rest] (split-at-less coll)]
    (if-let [swap (first rest)]
      (let [left (->> asc (take-while #(pos? (compare swap %))))
            [swap-with & right] (drop (count left) asc)
            result (concat left [swap] right [swap-with] (next rest))]
        (->> result reverse (apply str)))
      "no answer")))
