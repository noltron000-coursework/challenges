# == TASK ==
# Given an array of n numbers and a target value, t,
# find two numbers from the array whose sum is t.

# == EXAMPLE ==
# array = [5, 3, 6, 8, 2, 4, 7]
# (thus n = 7)
# t = 10
# results = [3, 7] or [6, 4] or [8, 2]

# == PSEUDOCODE ==
# create function named two_sum,
# that takes an array,
# and a target number, called t.

# 	create a new, empty set called pairs.
# 	it will hold what its pair must be to reach t.

# 	loop through each number in the array,
# 	in order of each entry's index.


# 		subtract t from the number to get its pair.

# 		check if the paired number is in the pairs set.

# 			if so, we have our pair. return the two numbers.

# 		otherwise, add the potential pair into the pairs set.

# 	if the loop ends, there is no pair in the original array.
# 	at this point one could return an error,
# 	or a value that represents nothing
