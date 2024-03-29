#lang racket

#|
Given an array of numbers nums, in which exactly two elements appear only
once and all the other elements appear exactly twice. Find the two elements
that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
1. The order of the result is not important. So in the above example,
[5, 3] is also correct.

2. Your algorithm should run in linear runtime complexity.
Could you implement it using only constant space complexity?
|#

(require rackunit)

(define (single-number xs)
  (let* ([t (foldl bitwise-xor 0 xs)]
         [ans (foldl bitwise-xor 0 (filter (λ (x) (zero? (bitwise-and x t (- t)))) xs))])
    `(,ans ,(bitwise-xor ans t))))

(check-equal? (single-number '(1 2 1 3 2 5)) '(5 3))