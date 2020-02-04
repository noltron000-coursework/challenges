# == TASK ==
# Given two arrays a and b of numbers and a target value t,
# find a number from each array whose sum is closest to t.

# == EXAMPLE ==
# a = [9, 13, 1, 8, 12, 4, 0, 5]
# b = [3, 17, 4, 14, 6]
# t = 20
# results = [13, 6] or [4, 17] or [5, 14]

# == PSEUDOCODE ==
def get_closest_pair(a, b, t):
	a = a[:]
	b = b[:]
	a.sort()
	b.sort()

	index_a = 0
	index_b = len(b) - 1

	best_pair = [a[index_a], b[index_b]]

	while index_a <= len(a) - 1 and index_b >= 0:
		# get current pair
		current_pair = [a[index_a], b[index_b]]
		# current pair is better than best pair
		if abs(sum(best_pair) - t) > abs(sum(current_pair) - t):
			best_pair = current_pair

		# increment pointer a
		if sum(current_pair) < t:
			if index_a == len(a) - 1:
				break
			index_a += 1

		# increment pointer b
		elif sum(current_pair) > t:
			if index_b == 0:
				break
			index_b -= 1

		# found an exact match;
		# sum(current_pair) == t
		else:
			break

	# best pair is found when loop is done
	return best_pair

# == TEST EXAMPLE ==
a = [9, 13, 1, 8, 12, 4, 0, 5]
b = [3, 17, 4, 14, 6]
t = 20
# results = [13, 6] or [4, 17] or [5, 14]

print(get_closest_pair(a, b, t))
