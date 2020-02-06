# == TASK ==
# You’re working an internship at Twitter and are tasked to improve suggestions for
# accounts to follow, which already works great for established accounts because it uses
# content from your tweets and other accounts you follow to suggest new ones. However,
# when a new user signs up none of this information exists yet, but Twitter still wants
# to make some follow suggestions. Your team asked you to implement a function that
# accepts a new user’s handle and an array of many other users’ handles, which could be
# very long – Twitter has over 330 million active accounts! You need to calculate a
# similarity score between a pair of handles by looking at the letters each contains,
# scoring +1 for each letter in the alphabet that occurs in both handles but scoring –1
# for each letter that occurs in only one handle. Your function should return k handles
# from the array that have the highest similarity score to the new user’s handle.

# == EXAMPLE ==
# new_handle = 'iLoveDogs'
# k = 2
# handles = set([
# 	'DogeCoin',
# 	'YangGang2020',
# 	'HodlForLife',
# 	'fakeDonaldDrumpf',
# 	'GodIsLove',
# 	'BernieOrBust'
# ])
# results: ['GodIsLove', 'DogeCoin']


# == CODE ==
class SortedArrayObject:
	def __init__(self):
		self.list = []

	def add(self, item):
		# convert list to immutable tuple
		item = tuple(item)
		# add item to array
		self.list.append(item)
		# sort by entry's score
		self.list.sort(key = lambda entry: entry[0])

	def get_max(self, k=1):
		return self.list[-k:]

# define a function that takes in three parameters:
# a new handle for a username,
# a list of handles to match up from,
# and a number of matches to be returned (default 1).
def most_similar_handles(handle, other_handles, k = 1):
	# create an object called best_names,
	# which will always be sorted by an entry's score.
	# it will contain a handle, and its associated score
	# with new_handle.
	handles_by_score = SortedArrayObject()

	# loop through each name in the handles list.
	for other_handle in other_handles:
		# set a variable, score, equal to get_score() helper
		# function to get the handle's associated score.
		score = get_score_single(handle, other_handle)
		# using add_item() helper function,
		# add the score and handle to the best_name object,
		# ensuring sorted order.
		handles_by_score.add([score, other_handle])

	# return the best k items from the best_names object.
	# this should be easy to do since the object is sorted.
	return handles_by_score.get_max(k)

# def get_score_single(handle1, handle2):
# 	# helper function
# 	def populate(handle):
# 		char_histogram = {}
# 		for char in handle1:
# 			if char in char_histogram:
# 				char_histogram[char] += 1
# 			else:
# 				char_histogram[char] = 1

# 	histo1 = populate(handle1)
# 	histo2 = populate(handle2)

# 	score = 0
# 	for char in smaller_histogram:
# 		if char in 

def get_score_single(handle1, handle2):

	# helper function
	def populate_set(handle):
		char_set = set()
		for char in handle1:
			char_set.add(char)
		print(char_set)
		return char_set

	# get basic sets
	set1 = populate_set(handle1)
	set2 = populate_set(handle2)
	# find score modifiers based on set info
	bonuses = set1.intersection(set2)
	penalties = set1.symmetric_difference(set2)
	print(bonuses)
	print(penalties)
	# get total score
	return len(bonuses) - len(penalties)


# == TEST EXAMPLE ==
new_handle = 'iLoveDogs'
k = 2
handles = set([
	'DogeCoin',
	'YangGang2020',
	'HodlForLife',
	'fakeDonaldDrumpf',
	'GodIsLove',
	'BernieOrBust'
])
# results: ['GodIsLove', 'DogeCoin']
print(most_similar_handles(new_handle, handles))
