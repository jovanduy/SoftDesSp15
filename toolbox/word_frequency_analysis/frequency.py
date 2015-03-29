""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	# with open(file_name, 'r') as fp:
	# 	for line in fp:
	# 		if line.startswith('*END*THE SMALL PRINT!'):
	# 			break
	f = open(file_name,'r')
	lines = f.readlines()
	curr_line = 0
	while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
		curr_line += 1
	lines = lines[curr_line+1:]
	word_list = []
	for line in lines:
		for word in line.split():
			word = string.lower(word)
			word = ''.join(char for char in word if char not in string.punctuation)
			word_list.append(word)
	return word_list
		


def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	word_counts = {}
	for word in word_list:
		word_counts[word] = 1 + word_counts.get(word, 0)
	return sorted(word_counts, key=word_counts.get, reverse=True)[:n]

if __name__ == '__main__':
	print get_top_n_words(get_word_list('pg32325.txt'), 100)

