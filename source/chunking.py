import sys, re

if __name__ == '__main__':
	inputFileName = sys.argv[-1]
	dotLocation = sys.argv[-1].index(".")
	outputFileName = inputFileName[:dotLocation] + '.crfsuite' + inputFileName[dotLocation:]
	outputFile = open(inputFileName[:dotLocation] + '.crfsuite' + inputFileName[dotLocation:], 'w')
	vowels = list("aeiou")
	consonants = list("bcdfghjklmnpqrstvexyz")
	with open(inputFileName, 'r') as inputFile:
		for line in inputFile:
			line = line.strip()
			code = ''
			if len(line) > 0:
				words = line.split()
				code = code + words[-1] + '\t'
				if words[-2] is '0':
					code = code + 'False' + '\t'
				else:
					code = code + 'True' + '\t'
				if words[-3] is '0':
					code = code + 'False' + '\t'
				else:
					code = code + 'True' + '\t'
				if words[-4] is '0':
					code = code + 'False' + '\t'
				else:
					code = code + 'True' + '\t'
				if words[-5] is '0':
					code = code + 'False' + '\t'
				else:
					code = code + 'True' + '\t'
				code = code + words[-6] + '\t' + words[-7]
				n_words = len(line) - 6
				code = code + `n_words` + '\n'
				outputFile.write(code)
			else:
				outputFile.write('\n')
