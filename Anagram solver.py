user_input = input('Enter  your anagram: ')
from itertools import permutations
spel = [''.join(data) for data in permutations(user_input)]
for i in spel:
	with open("WordList.txt", "r") as a_file:
		for line in a_file:
		    stripped_line = line.strip()
		    if i == stripped_line:
		    	print(stripped_line)