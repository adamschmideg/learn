(ns its4clojure.core-test
  (:require [clojure.test :refer :all]
            [its4clojure.core :refer :all]))

(deftest fibonacci-test
  (is (= (fibonacci 1) [1]))
  (is (= (fibonacci 3) [1 2 1]))
  (is (= (fibonacci 4) [1 3 3 1])))

(deftest my-flatten-test
  (are [xs want] (= want (my-flatten xs))
    3 3
    [4] [4]
    [2 5] [2 5]
    [[7]] [7]
    [[[8]]]              [8]
    [nil]  [nil]
    [[]]                 []
    [] []
    [1 [2] 3] [1 2 3]
    [1 [2 [3 4] 5] 6] [1 2 3 4 5 6]))

(deftest btree?-test
  (are [tree b?] (= b? (btree? tree))
    '(:a (:b nil nil) nil) true
    [1 2 3 4]  false
    [1 nil [2 [3 nil nil] [4 nil nil]]] true
    [1 [2 nil nil] [3 nil nil] [4 nil nil]] false
    [4 false nil] false))

(run-all-tests #"its4clojure.core-test/btree?-test")