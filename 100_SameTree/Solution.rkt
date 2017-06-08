#lang racket

(require rackunit)

#|
Given two binary trees, write a function to check if they
are equal or not.

Two binary trees are considered equal if they are structurally 
identical and the nodes have the same value.
|#

(struct End ())
(struct Tree (val left right))

(define (same-tree? p q)
  (match `(,p ,q)
    [`(,(End) ,(End)) #t]
    [`(,(Tree v1 l1 r1) ,(Tree v2 l2 r2))
     (and (eq? v1 v2) (same-tree? l1 l2) (same-tree? r1 r2))]
    [_ #f]))

(module+ test
  (define t1
    (Tree 1 (End) (End)))
  (define t2
    (Tree 2 (End) (End)))
  (define t3
    (Tree 1
          (Tree 2 (End) (End))
          (Tree 3 (End) (End))))
  (define t4
    (Tree 1
          (Tree 2 (End) (End))
          (Tree 3 (End) (End))))
  
  (check-eq? (same-tree? t1 t2) #f)
  (check-eq? (same-tree? t3 t4) #t))