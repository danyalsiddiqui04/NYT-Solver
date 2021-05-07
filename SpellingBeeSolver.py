# python spellingbeesolver.py
# Made by Danyal Siddiqui
# 5/7/2021
# Solves any New York Times spelling bee puzzle

# allows us to remove duplicates from list
from collections import OrderedDict

# file that contains ~450,000 English words
words = open('words.txt')
# asks for the hexagon letters and puts in list
letters = list(input('Input all the letters in the hexagon, CENTER LETTER FIRST: '))
# this is the center letter
center = letters[0]
# center letter is removed from list and list is sorted
letters.sort()
letters.remove(center)
# this is where all the words will be stored in case the user wants to save
all_words = []

# parses each word in the file
for word in words:
	go = True
	# must be 4 letters or more (puzzle rules)
	if len(word) >= 4:
		# removes duplicate letters from word and returns list
		rd = list(OrderedDict.fromkeys(list(word.lower())))
		# remove newline character and sort the list
		rd.pop(-1)
		rd.sort()

		# check if word contains center letter
		if center in rd:
			# remove the center letter from word
			rd.remove(center)
			# check each letter against input letters
			for letter in rd:
				if letter not in letters:
					go = False
			# if the word contains only correct letters, then print it
			if go == True:
				print(word)
				all_words.append(word)

# asks the user if they want to end or save
end = input('Press enter to quit or type "save" to save to a file: ')
if end == 'save':
	# create file if does not already exist
	answers = open('answers.txt', 'w')
	for i in all_words:
		answers.write(i)
	print('Your words have been stored in the "answers" file!')