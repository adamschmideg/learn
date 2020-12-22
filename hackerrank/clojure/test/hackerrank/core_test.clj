(ns hackerrank.core-test
  (:require [clojure.test :refer :all]
            [hackerrank.core :refer :all]))

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
      "madamimadam" 4 7 2)))
