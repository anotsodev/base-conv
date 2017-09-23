# Just a simple BaseX converter.
# Used different methods that were found on the Internet to convert text or numbers to different number systems.
#
# Requirements:
# 	Python 2.x.x
#
# Usage:
# python basex-conv.py b64 1
# 

import sys
import binascii

MODES = ['b2','b8','b16','b64']

def converter(FIRST_ARG, SECOND_ARG):
	if FIRST_ARG in MODES:
		if FIRST_ARG == 'b2':
			result = bin(int(binascii.hexlify(SECOND_ARG), 16))[1:] # https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
			result = " ".join(result[i:i+8] for i in range(0, len(result), 8)) # https://stackoverflow.com/questions/10055631/how-do-i-insert-spaces-into-a-string-using-the-range-function
			print result
		elif FIRST_ARG == 'b8':
			result = " ".join([oct(ord(char)) for char in SECOND_ARG]) # http://pythonjourney.com/python-convert-string-to-binary-octal-hex/
			print result
		elif FIRST_ARG == 'b16':
			result = " ".join([hex(ord(char)) for char in SECOND_ARG])
			print result
		elif FIRST_ARG == 'b64':
			print binascii.b2a_base64(SECOND_ARG)
		else:
			print "Usage: python basex-conv.py <b2 | b8 | b16 | b64> <text or number>"
	else:
		print "Usage: python basex-conv.py <b2 | b8 | b16 | b64> <text or number>"


if __name__ == "__main__":
	try:
		FIRST_ARG = sys.argv[1]
		SECOND_ARG = sys.argv[2]
		converter(FIRST_ARG, SECOND_ARG)
	except:
		print("Usage: python basex-conv.py <b2 | b8 | b16 | b64> <string or number>")
		sys.exit(1)