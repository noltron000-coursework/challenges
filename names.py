'''
Given a sorted array of strings, write a recursive function
to find the index of the first and last occurrence of a
target string. If the target string is not found in the
array, report that.

Example inputs:
- instructors = ['Adriana', 'Adriana', 'Alan', 'Alan', 'Alan', 'Alan', 'Alan', 'Braus', 'Braus', 'Braus', 'Braus', 'Dan', 'Dan', 'Dan', 'Dan', 'Dan', 'Dani', 'Dani', 'Jess', 'Meredith', 'Milad', 'Milad', 'Mitchell', 'Mitchell', 'Mitchell', 'Mitchell']
- target = 'braus'
Example execution:
- find_indexes(instructors, target) => (7, 10)
'''


make_instructors = [
	'Adriana', 'Adriana',
	'Alan', 'Alan', 'Alan', 'Alan', 'Alan',
	'Braus', 'Braus', 'Braus', 'Braus',
	'Dan', 'Dan', 'Dan', 'Dan', 'Dan',
	'Dani', 'Dani',
	'Jess',
	'Meredith',
	'Milad', 'Milad',
	'Mitchell', 'Mitchell', 'Mitchell', 'Mitchell',
]


def find_indexes(instructors, target):
	# find location of one target occurance
	search_index = binary_search(instructors, target)[0]
	# just in case there is no value
	if search_index == None:
		return None, None

	# find location of first target occurance
	first_index = search_index
	while instructors[first_index - 1] == target:
		first_index -= 1
	
	# find location of final target occurance
	final_index = search_index
	while instructors[final_index + 1] == target:
		final_index += 1
		
	# return locations of first and last target
	return first_index, final_index


def binary_search(instructors, target, min_index=None, max_index=None):
	# initialize for recursive check
	if min_index is None:
		min_index = 0
	if max_index is None:
		max_index = len(instructors)

	# base case: no results found
	if min_index == max_index:
		return None, None

	med_index = (min_index + max_index) // 2
	# get the middle of the instructors array
	med_value = instructors[med_index]

	# recursively search if needed,
	# else return the current median
	if target == med_value:
		return med_index, med_value
	elif target < med_value:
		return binary_search(instructors, target, min_index, med_index)
	elif target > med_value:
		return binary_search(instructors, target, med_index+1, max_index)
	else:
		raise ValueError('weird!')


print(find_indexes(
	make_instructors, 'Braus'
))
