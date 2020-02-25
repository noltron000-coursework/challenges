# FizzBuzz
# -> takes integer: start
# -> takes integer: end

# returns:
# -> fizzbuzzified list of ranges (start...finish)

def _fizz_buzz_iterative(start, end):
	results = list(range(start, end + 1))
	for index, value in enumerate(results):
		results[index] = foobar(value)
	return results

def _fizz_buzz_recursive(start, end, results=None):
	if results is None:
		results = []

	results.append(foobar(start))

	if start == end:
		return results
	else:
		return _fizz_buzz_recursive(start+1, end, results)

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

print(_fizz_buzz_iterative(1, 20))
print(_fizz_buzz_recursive(1, 20))
