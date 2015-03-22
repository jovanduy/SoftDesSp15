"""
@author: Jordan Van Duyne

Performs Markov analysis on n number of texts, combining the language of the text(s)
to create a new work.

To run: markov.py filename-1 filename-2 ... filename-n #OfWords
"""

import sys
import string
import random

prefix_to_suffix = dict()

def read_file(filename):
    """
    Reads through filename, updating the global tuple prefix and adding suffixes
    to the global dictionary prefix_to_suffix for each word and the word before it.

    filename: path to file
    prefix_len: integer length of the "prefix" being used for analysis
    """
    prefix = ()
    prefix_len = 2
    with open(filename, 'r') as fp:
    	for line in fp:
        	for word in line.rstrip().split():
        		if len(prefix) < prefix_len:
        			prefix += word,
        		else:
	        		if prefix in prefix_to_suffix:
	        			prefix_to_suffix[prefix].append(word)
	        		else:
	        			prefix_to_suffix[prefix] = [word]
	    			prefix = prefix[1:] + (word,)

def new_text(num_words):
    """
    Creates num_words words based randomly off the entries in prefix_to_suffix.

    num_words: integer number of words to print

    returns: string containing all words of the new text
    """
    global prefix_to_suffix #don't have to do this, you aren't re-writing the global dictionary
    prefix = random.choice(prefix_to_suffix.keys())
    s = ''
    for element in prefix:
    	s += element + ' '
    for i in range(int(num_words)-2):
    	word = random.choice(prefix_to_suffix[prefix])
    	s += word + ' '
    	prefix = prefix[1:] + (word,)
    return s

if __name__ == '__main__':
    arguments = sys.argv
    if len(arguments) < 2:
    	print 'Please have arguments be: filename-1 filename-2 ... filename-n #OfWords'
    else:
    	for i in range(1, len(arguments)-1):
    		read_file(arguments[1])
    	with open('NewText.txt', 'a') as fp:
    		fp.write(new_text(arguments[-1]))
