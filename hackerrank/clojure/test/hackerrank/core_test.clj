(ns hackerrank.core-test
  (:require [clojure.test :refer :all]
            [hackerrank.core :refer :all]
            [clojure.java.io :as io]))

(deftest maximum-palindromes-test
  (testing "length"
    (are [s len] (= len (max-palindrome-length s))
      "baba" 4
      "baca" 3
      "babab" 5
      "abaca" 3))
  (testing "short and sweet"
    (are [s n] (= n (maximum-palindromes s))
      "aaaa" 1
      "abab" 2
      "bababb" 3
      "amim" 2))
  (testing "short"
    (are [s start end n] (= n (maximum-palindromes s start end))
      "madamimadam" 4 7 2))
  (testing "test case 12"
    (let [s "wldsfubcsxrryqpqyqqxrlffumtuwymbybnpemdiwyqz"]
      (are [start end n] (= n (maximum-palindromes s start end))
        31 38 8
        29 33 3
        13 34 60480
        4 17 144
        15 26 16
        2 10 7
        10 33 544320)))
  (testing "from resource"
    (let [input (-> "resources/input.txt" io/resource slurp)])))

