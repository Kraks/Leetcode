#lang racket

(require rackunit)

#|
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest End node.
|#

(struct End () #:transparent)
(struct Tree (val left right) #:transparent)

(define (max-depth root)
  (define (aux node depth)
    (cond [(End? node) depth]
          [(Tree? node)
           (max (aux (Tree-left node) (+ 1 depth))
                (aux (Tree-right node) (+ 1 depth)))]))
  (aux root 0))

(module+ test
  (define t1
    (Tree 1 (End) (End)))
  
  (define t2
    (Tree 1
          (Tree 2
                (Tree 3 (End) (End))
                (End))
          (End)))

  (define t3
    (Tree 1
          (Tree 2
                (Tree 3 (End) (End))
                (Tree 4
                      (Tree 5 (End) (End))
                      (End)))
          (End)))

  (check-eq? 1 (max-depth t1))
  (check-eq? 3 (max-depth t2))
  (check-eq? 4 (max-depth t3)))
