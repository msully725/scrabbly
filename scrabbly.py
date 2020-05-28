#
# scrabbly
#
import sys

if len(sys.argv) != 3:
	print "blarg (incorrect parameters)"
	print "letters spaces"
	print "i.e. aahgjk __ll_"
	sys.exit(0)

letters = sys.argv[1]
spaces = sys.argv[2]

# Load all words
wordList = [ ]
fWordList = open('ospd.txt', 'r')

for line in fWordList:
	line = line.strip()

	if len(line) != len(spaces):
		continue

	skipLine = False

	for i in range(len(spaces)):
		if (spaces[i] == '_'):
			if letters.count(line[i]) < line.count(line[i]):
				skipLine = True
		elif spaces[i] != line[i]:
			skipLine = True

	if not skipLine:
		# line fits our letters and spaces, add it
		wordList.append(line)

print "Results:"

for word in wordList:
	print word

print "Total Matches: " + str(len(wordList))
