"""
@author: Jordan Van Duyne

Used to create a .txt file from text taken Project Gutenberg.

To run: get_txt.py URLofProjectGutenbergTxtPage
"""
from pattern.web import *

if __name__ == '__main__':
	text = URL(sys.argv[1]).download()
	with open('HuckFinn.txt', 'a') as fp:
		fp.write(text)