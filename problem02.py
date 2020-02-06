import math
infinity = math.inf

# == TASK ==
# Given an array of n numbers and a count k,
# find the k largest values in the array.

# == EXAMPLE ==
# array = [5, 1, 3, 6, 8, 2, 4, 7]
# (thus n = 8)
# k = 3
# results = [6, 8, 7]

# == CODE ==
def get_top_k_naive(array, k):
	# create a sorted copy of the array
	array = array[:]
	array.sort()
	# return the final k values of the array.
	return array[-k:]

def get_top_k(array, k):
	# get a list of size k
	# containing only negative infinities
	top_scores = [-infinity] * k
	for number in array:
		i = 0
		while i < len(top_scores): # [5, 3, 2, 4]
			if number > top_scores[i]: # [2, 3, 5]
				i += 1 # yes increase
			else:
				top_scores.insert(i, number) # number = -1 -> [2, 3, 5]
				top_scores = top_scores[1:] # [2, 3, 5]
				break
		else:
			top_scores.insert(i, number)
			top_scores = top_scores[1:]
	return top_scores

# == TEST EXAMPLE ==
array = [5, 1, 3, 6, 8, 2, 4, 7]
# (thus n = 8)
k = 3
# results = [6, 8, 7]
print(get_top_k(array, k))
