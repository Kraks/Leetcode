#lang racket

(require rackunit)

#|
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9

to

     4
   /   \
  7     2
 / \   / \
9   6 3   1

|#

(struct End () #:transparent)
(struct Tree (val left right) #:transparent)

(define (invert-tree t)
  (cond [(End? t) t]
        [(Tree? t)
         (Tree (Tree-val t)
               (invert-tree (Tree-right t))
               (invert-tree (Tree-left t)))]))

(module+ test
  (define t1
    (Tree 1
          (Tree 2 (End) (End))
          (Tree 3 (End) (End))))
  
  (check-equal? (invert-tree t1)
                (Tree 1 (Tree 3 (End) (End)) (Tree 2 (End) (End))))
  
  (define t2
    (Tree 4
          (Tree 2
                (Tree 1 (End) (End))
                (Tree 3 (End) (End)))
          (Tree 7
                (Tree 6 (End) (End))
                (Tree 9 (End) (End)))))
  
  (check-equal? (invert-tree t2)
                (Tree
                 4
                 (Tree
                  7
                  (Tree 9 (End) (End))
                  (Tree 6 (End) (End)))
                 (Tree
                  2
                  (Tree 3 (End) (End))
                  (Tree 1 (End) (End))))))