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
  (testing "from resource"))

(deftest bigger-is-greater-test
  (testing "split-at-ascending"
    (is (= [[1 3] [2 0]] (split-at-less [1 3 2 0])))
    (is (= [[1 2 3] []] (split-at-less [1 2 3])))
    (is (= [[3] [2 1]] (split-at-less [3 2 1]))))
  (testing "max-index"
    (is (= 1 (max-index [:b :z :a :f]))))
  (testing "bigger-is-greater"
    (is (= "lmon" (biggest-is-greater "lmno")))
    (is (= "no answer" (biggest-is-greater "dcba")))))