#lang typed/racket

(require math/number-theory)

(: soph-prime? : Integer -> Boolean)
(define (soph-prime? int) (local {
	(: div-check : Integer Integer -> Boolean)
	(define (div-check i div) (cond 
		[(= i div) #t]
		[(= (modulo i div) 0) #f]
		[else (div-check i (+ div 1))]))}
	(div-check int 2)))

(: big-prime-fact : Integer -> Integer)
(define (big-prime-fact num) (local {
	(: prime-facts : Integer Integer (Listof Integer)  -> (Listof Integer))
	(define (prime-facts n div acc) (cond
		[(= n div) (cons div acc)]
		[(and (= (modulo n div) 0) (soph-prime? div)) (prime-facts (/ n div) div (cons div acc))]
		[else (prime-facts n (+ div 1) acc)]))}
	(first (prime-facts num 2 '())))) 

(big-prime-fact 2)
(big-prime-fact 12)
(big-prime-fact 20)
(big-prime-fact 300)
(big-prime-fact 600851475143)




