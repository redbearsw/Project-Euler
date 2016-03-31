#lang typed/racket

(: fibonacci : Integer -> Integer)
;given a term, n, produces the fibonacci number for that n
(define (fibonacci n) (cond
	[(= n 1) 1]
	[(= n 2) 2]
	[else (+ (fibonacci (- n 1)) (fibonacci (- n 2)))]))

(fibonacci 3)
(fibonacci 4)
(fibonacci 32)
(fibonacci 33)
(fibonacci 34)
(fibonacci 13)
(fibonacci 14)

(: fib-4-mil : Integer -> Integer)
;returns the term of the fibonacci number that is the largest below 4 million
(define (fib-4-mil acc) (cond
	[(>= (fibonacci acc) 4000000) (- acc 1)]
	[else (fib-4-mil (+ 1 acc))]))

(fib-4-mil 20)

(: even-fibs : Integer -> Integer)
;sums the even fibs up to the nth term
(define (even-fibs n) (local {
	(: even-fibs-acc : Integer Integer -> Integer)
	(define (even-fibs-acc n acc) (cond
		[(= n 0) acc]
		[(= (modulo (fibonacci n) 2) 0) (even-fibs-acc (- n 1) (+ (fibonacci n) acc))]
		[else (even-fibs-acc (- n 1) acc)]))}
	(even-fibs-acc n 0)))

(even-fibs 34)
