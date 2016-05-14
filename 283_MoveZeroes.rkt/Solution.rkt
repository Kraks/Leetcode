#lang racket

(require rackunit)

#|
Given an array nums, write a function to move all 0's to the end of
it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function,
nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
|#

(define (move-zeroes nums)
  (cond [(null? nums) '()]
        [(zero? (car nums)) (append (move-zeroes (cdr nums)) '(0))]
        [else (cons (car nums) (move-zeroes (cdr nums)))]))

(module+ test
  (check-equal? (move-zeroes '(0 1 0 3 12)) '(1 3 12 0 0))
  (check-equal? (move-zeroes '(0 0 0 1 2 3)) '(1 2 3 0 0 0)))