#lang racket

(require rackunit)

#|
Write a function to delete a node (except the tail) in a singly linked list,
given only access to that node.

Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third
node with value 3, the linked list should become 1 -> 2 -> 4 after calling
your function.
|#

(struct End () #:transparent)
(struct Node (val next) #:transparent #:mutable)

(define (delete-node node)
  (set-Node-val! node (Node-val (Node-next node)))
  (set-Node-next! node (Node-next (Node-next node)))
  node)

(module+ test
  (define lst
    (Node 1 (Node 2 (Node 3 (Node 4 (End))))))
  
  (check-equal? (delete-node (Node-next lst))
                (Node 3 (Node 4 (End))))
  
  (check-equal? lst
                (Node 1 (Node 3 (Node 4 (End))))))