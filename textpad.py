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

t9_num_to_letter = {
	0: [
		' '  # space-character
	]
	1: [
		',',
		'.',
		'?',
		'!',
	]
	2: [
		'a',
		'b',
		'c',
	],
	3: [
		'd',
		'e',
		'f',
	],
	4: [
		'g',
		'h',
		'i',
	],
	5: [
		'j',
		'k',
		'l',
	],
	6: [
		'm',
		'n',
		'o',
	],
	7: [
		'p',
		'q',
		'r',
		's',
	],
	8: [
		't',
		'u',
		'v',
	],
	9: [
		'w',
		'x',
		'y',
		'z',
	],
}
