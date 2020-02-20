# FizzBuzz
# -> takes integer: start
# -> takes integer: end

# returns:
# -> fizzbuzzified list of ranges (start...finish)

# RECURSIVE OPTIONS

def fizz_buzz(start, end):
	results = list(range(start, end + 1))
	for index, value in enumerate(results):
		results[index] = foobar(value)
	return results

def foobar(number):
	string = ''
	if number % 3 == 0:
		string += 'Fizz'
	if number % 5 == 0:
		string += 'Buzz'
	if string != '':
		return string
	else:
		return number

print(fizz_buzz(1, 20))
