#lang typed/racket

(: prime-facts : Integer -> (Listof Integer))
;returns largest prime factor
(define (prime-facts n) (local {
	(: primes-acc : Integer (Listof Integer) -> (Listof Integer))
	(define (primes-acc num acc) (cond 
		[(prime? num) (cond
			[(= num 1) acc]
			[(= (modulo n num) 0) 
				(primes-acc (- num 1) (cons num acc))]
			[else (primes-acc (- num 1) acc)])
		[else (primes-acc (- num 1) acc)]))}
	(primes-acc n '())))

(prime-facts 13195)
(prime-facts 600851475143) 
	

;start with num
;if prime, check if modulo =0
;if both true, cons
;else check next number
