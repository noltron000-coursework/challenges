# == TASK ==
# Given an array of n numbers and a target value, t,
# find two numbers from the array whose sum is t.

# == EXAMPLE ==
# array = [5, 3, 6, 8, 2, 4, 7]
# (thus n = 7)
# t = 10
# results = [3, 7] or [6, 4] or [8, 2]

# naive approach
def two_sum_naive(array, t):
	for i in array:
		for j in array:
			if i != j and i + j == t:
				return i, j

# == CODE ==
def two_sum(array, t):
	# checked_values holds valid complements used to reach t.
	checked_values = set()

	# crawl through the array by each number
	for number in array:
		# whats this number's complement to be a solution?
		complement = t - number
		# is this number a valid complement of another?
		if complement in checked_values:
			return complement, number
		else:
			# otherwise add the needed number into checked_values
			checked_values.add(number)

	# no matches
	return None

# == TEST EXAMPLE ==
array = [5, 3, 6, 8, 2, 4, 7]
# (thus n = 7)
t = 10
# results = [3, 7] or [6, 4] or [8, 2]
print(two_sum(array, t))
