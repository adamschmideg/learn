(ns its4clojure.core-test
  (:require [clojure.test :refer :all]
            [its4clojure.core :refer :all]))

(deftest pascal-test
  (is (= (pascal 1) [1]))
  (is (= (pascal 3) [1 2 1]))
  (is (= (pascal 4) [1 3 3 1])))

(deftest my-flatten-test
  (are [xs want]
    (= want (my-flatten xs))
    3 3
    [4] [4]
    [2 5] [2 5]
    [[7]] [7]
    [[[8]]] [8]
    [nil] [nil]
    [[]] []
    [] []
    [1 [2] 3] [1 2 3]
    [1 [2 [3 4] 5] 6] [1 2 3 4 5 6]))

(deftest btree?-test
  (are [tree b?]
    (= b? (btree? tree))
    '(:a (:b nil nil) nil) true
    [1 2 3 4]  false
    [1 nil [2 [3 nil nil] [4 nil nil]]] true
    [1 [2 nil nil] [3 nil nil] [4 nil nil]] false
    [4 false nil] false))

(deftest map-test
  (is (= [1 2 3] (my-map inc [0 1 2])))
  (is (= 5 (count (take 5 (my-map inc (range 100000)))))))

(deftest lcm-test
  (is (= 6 (lcm 2 3)))
  (is (= 105 (lcm 5 3 7))))

(deftest un-interleave-test
  (is (= [[0 2 4] [1 3 5]] (un-interleave (range 6) 2))))

(run-all-tests #"its4clojure.core-test/btree?-test")