#lang racket

(require rackunit)

#|
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Hint: http://www.wikiwand.com/en/Digital_root
|#

(define (add-digits n)
  (+ 1 (modulo (- n 1) 9)))

(module+ test
  (check-eq? 2 (add-digits 38))
  (check-eq? 8 (add-digits 467)))
