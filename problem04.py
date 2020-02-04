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

# == PSEUDOCODE ==
# define a function that takes in three parameters:
# a new handle for a username,
# a list of handles to match up from,
# and a number of matches to be returned (default 1).

# 	create an object called best_name,
# 	which will always be sorted by an entry's score.
# 	it will contain a handle, and its associated score
# 	with new_handle.

# 		loop through each name in the handles list.

# 			set a variable, score, equal to get_score() helper
# 			function to get the handle's associated score.

# 			using add_item() helper function,
# 			add the score and handle to the best_name object,
# 			ensuring sorted order.

# 		return the best k items from the best_names object.
# 		this should be easy to do since the object is sorted.
