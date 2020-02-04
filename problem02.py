# == TASK ==
# Given an array of n numbers and a count k,
# find the k largest values in the array.

# == EXAMPLE ==
# array = [5, 1, 3, 6, 8, 2, 4, 7]
# (thus n = 8)
# k = 3
# results = [6, 8, 7]

# == PSEUDOCODE ==
def find_top_k(array, k):
	# create a sorted copy of the array
	array = array[:].sort()
	# return the final k values of the array.
	return array[array.length - k:]
