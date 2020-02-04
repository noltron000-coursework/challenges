# == TASK ==
# Given two arrays a and b of numbers and a target value t,
# find a number from each array whose sum is closest to t.

# == EXAMPLE ==
# a = [9, 13, 1, 8, 12, 4, 0, 5]
# b = [3, 17, 4, 14, 6]
# t = 20
# results = [13, 6] or [4, 17] or [5, 14]

# == PSEUDOCODE ==
# create a new function called get_closest_pair
# that takes three inputs, including two arrays of numbers,
# (called a and b), and a target number t.

# 	create a copy of array a and sort it

# 	create a copy of array b and sort it

# 	create a pointer to the smallest item in a,
# 	based on the index of a or keeping track of it

# 	create a pointer to the largest item in b,
# 	based on the index of b or keeping track of it

# 	create an array of size two containing
# 	the current value of those two pointers.
# 	call the array best_pair;
# 	this array will be updated with better pairs
# 	as this runs, based on their sum's difference to t.

# 	loop while pointer a can get larger,
# 	or pointer b can get smaller,

# 		get the sum of pointers a and b.

# 		check if the current pointers' sum are better than
# 		best_pair's sum.

# 			if it is, replace best_pair with the new best pair.

# 		if the sum is larger than t,

# 			check if pointer a can't get larger...

# 				if it can't, break the while loop.

# 				otherwise, increase pointer a
# 				to the next larger item

# 		else, if the sum is smaller than t,

# 			check if pointer b can't get smaller...

# 				if it can't, break the while loop.

# 				otherwise, decrease pointer b
# 				to the next smaller item.

# 		otherwise, if they are equal

# 			that's great! we can flat out return the pair right away.

# 	the loop broke if it ever got here.
# 	there is no exact match so just return best_pair.

# == TEST EXAMPLE ==
