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
	# find location of first target occurance
	# find location of last target occurance
	# return locations of first and last target