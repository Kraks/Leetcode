#lang racket

(require rackunit)

#|
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
|#

(define (single-number nums)
  (foldl bitwise-xor 0 nums))

(module+ test
  (check-eq? 1 (single-number '(1 2 2 3 3)))
  (check-eq? 2 (single-number '(1 1 3 3 2))))
