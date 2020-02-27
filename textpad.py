"""
PROMPT
======

Given a string of digits 2-9 a user has pressed on a T9
"old school" telephone keypad, return a list of all letter
combinations they could have been trying to type.

Example execution 1:
- input:	t9_letters("23")
- output:	["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

Example execution 2:
- input:	t9_letters("4663")
- output:	["gmmd", ..., "gone", ..., "good", ..., "home", ..., "hood", ..., "ioof"]
"""

t9_num_to_letters = {
	'0': [  # dictionary of arrays used.
		' ',  # space-character.
	],
	'1': [
		',',
		'.',
		'?',
		'!',
	],
	'2': [
		'a',
		'b',
		'c',
	],
	'3': [
		'd',
		'e',
		'f',
	],
	'4': [
		'g',
		'h',
		'i',
	],
	'5': [
		'j',
		'k',
		'l',
	],
	'6': [
		'm',
		'n',
		'o',
	],
	'7': [
		'p',
		'q',
		'r',
		's',
	],
	'8': [
		't',
		'u',
		'v',
	],
	'9': [
		'w',
		'x',
		'y',
		'z',
	],
}

def t9_letters(rmn_string, prv_combos=None):
	if prv_combos is None:
		prv_combos = ['']
	if rmn_string == '':
		return prv_combos

	num = rmn_string[0]
	rmn_string = rmn_string[1:]

	possible_letters = t9_num_to_letters[num]
	new_combos = []

	for combo in prv_combos:
		for letter in possible_letters:
			new_combos.append(combo + letter)

	return t9_letters(rmn_string, new_combos)

print(t9_letters('23'))
print(t9_letters('4663'))
