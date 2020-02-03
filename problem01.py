# == TASK ==
# Given an array of n numbers and a target value, t,
# find two numbers from the array whose sum is t.

# == EXAMPLE ==
# array = [5, 3, 6, 8, 2, 4, 7]
# (thus n = 7)
# t = 10
# results = [3, 7] or [6, 4] or [8, 2]

# == PSEUDOCODE ==
def two_sum(array, t):
	# pairs will hold what valid pairs must be to reach t.
	pairs = set()

	# crawl through the array by each number
	for number in array:
		# get what this number's pair must be to be a solution
		pair = number - t
		# check this number to see if its a pair of another
		if number in pairs:
			return pair, number
		else:
			# otherwise add the needed number into pairs
			pairs.add(pair)

	# no matches
	return None
