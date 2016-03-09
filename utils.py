import math


def fib_list(n):
	'''Returns a list of the Fibonacci numbers less than or equal to n.'''
	fib_list_ = [1, 1]

	while fib_list_[-1] <= n:
		fib_list_.append(fib_list_[-1] + fib_list_[-2])

	return fib_list_


def prime_list(n):
	'''Uses the Sieve of Eratasthones to return a list of primes less 
	than n.'''
	composite_list = [False] * (n + 1)
	prime_list_ = []

	for i in range(2, n + 1):
		if composite_list[i]:
			continue
		for j in xrange(2 * i, n + 1, i):
			composite_list[j] = True
		prime_list_.append(i)

	return prime_list_


def prime_factors(n):
	'''Returns the prime factorization of n as a list.'''
	prime_factors_ = []
	d = 2

	while d * d <= n:
		while n % d == 0:
			prime_factors_.append(d)
			n /= d
		d += 1
	if n > 1:
		prime_factors_.append(n)

	return prime_factors_


def gcd(a, b):
	'''Returns the greatest common divisor of a and b using
	the Euclidean Algorithm.'''
	while b != 0:
		r, b = b, a % b
		a = r

	return a


def lcm(a, b):
	'''Returns the least common multiple of a and b.'''

	return abs(a * b) / gcd(a, b)


def is_prime(n):
	'''Test to determine if a number n is prime.'''
	if n == 1: return False
	if n == 2: return True
	if n % 2 == 0: return False

	for d in range(3, int(math.sqrt(n)) + 1, 2):
		if n % d == 0:
			return False
	return True


def triangle(n):
	'''Returns the nth triangular number.'''
	return n * (n + 1) / 2


def n_div(n):
	'''Returns the number of divisors of n.'''
	prime_factors_ = prime_factors(n)
	n_div_ = 1

	for p in set(prime_factors_):
		n_div_ *= prime_factors_.count(p) + 1

	return n_div_



