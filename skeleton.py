import math

def fibonacci(n):
	'''
	Returns the n'th fibonacci number.
	'''
	a,b = 1,1
 	for i in range(n-1):
  		a,b = b,a+b
 	return a

def fizzbuzz(n):
	'''
	Returns fizz if n % 3, buzz if n % 5, and fizzbuzz if both
	'''
	if (n % 3 == 0) and (n % 5 == 0):
		return "fizzbuzz"
	elif (n % 3 == 0):
		return "fizz"
	elif (n % 5 == 0):
		return "buzz"
	else:
		return n

def reverse_string(s):
	'''
	Reverses and returns the input string
	'''
	return s[::-1]

def reverse_order_of_words(s):
	'''
	Reverses the ordering of the words in a string, does not reverse the words themselves
	'''
	word_list = s.split(' ')
	return word_list[::-1]

def is_prime(n):
	'''
	Returns true if n is a prime, false otherwise
	'''
	if n == 2: 
		return True
	if n < 2 or n % 2 == 0: 
		return False
	return not any(n % i == 0 for i in range(3, int(math.sqrt(n)) + 1, 2))

def get_nth_first_primes(n):
	'''
	Returns a list of the n-th first prime numbers
	'''
	primes = list()
	current = 0
	while len(primes) != n:
		if is_prime(current):
			primes.append(current)
		current += 1
	return primes

def get_nth_prime_number(n):
	'''
	Returns the nth prime number
	'''
	return get_nth_first_primes(n)[-1]

def main():
	

if __name__ == "__main__":
	main()