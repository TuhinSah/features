import sys, re
from string import ascii_letters, digits

if __name__ == '__main__':
	outputFile = open('training.txt', 'w')
	with open(sys.argv[-1], 'r') as inputFile:
		for line in inputFile:
			token = line.strip()
			if len(token) > 0:
				firstCharacter = token[0]
				lastCharacter = token[len(token) - 1]
				if re.search('[a-zA-Z]', token):
					hasLetters = 1
				else:
					hasLetters = 0
				if re.search('[A-Z]', token):
					hasUpperCase = 1
				else:
					hasUpperCase = 0
				if re.search('[0-9]', token):
					hasNumbers = 1
				else:
					hasNumbers = 0
				if any(c not in ascii_letters + digits for c in token):
					hasSymbols = 1
				else:
					hasSymbols = 0
				outputFile.write(token + ' ' + firstCharacter + ' ' + lastCharacter + ' ' + `hasLetters` + ' ' + `hasUpperCase` + ' ' + `hasNumbers` + ' ' + `hasSymbols` + '\n')
			else:
				outputFile.write('\n')
				