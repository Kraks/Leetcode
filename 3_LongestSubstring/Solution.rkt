#lang racket

(require rackunit)

(define (solution str)
  (define (helper str cur start longest h)
    (cond [(empty? str) longest]
          [(hash-has-key? h (car str))
           (define v (hash-ref h (car str)))
           (define new-start (if (>= v start) (add1 v) start))
           (helper (cdr str) (add1 cur)
                   new-start
                   (max longest (add1 (- cur new-start)))
                   (hash-update h (car str) (λ (x) cur)))]
          [else (helper (cdr str) (add1 cur) start (max longest (add1 (- cur start)))
                        (hash-set h (car str) cur))]))
  (helper str 0 0 0 (make-immutable-hash)))

(check-eq? (solution '(a b c a)) 3)
(check-eq? (solution '(b b b b)) 1)
(check-eq? (solution '(p w w k e w)) 3)
(check-eq? (solution '(a)) 1)
(check-eq? (solution '()) 0)
(check-eq? (solution '(a a b)) 2)
(check-eq? (solution '(t m m z u x t)) 5)