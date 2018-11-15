__doc__="""
    - Takes in a plain text file, "source-text.txt"
    - Makes it into a unique list of words
    - Filters words to only be words containing letters from "coolLetters" 
"""

########################################
#### change these lists as you wish ####

# words with letters here will be saved
coolLetters = "á à ã â é ê ç í ó ô õ ú ü"

# be sure to use backslash to escape from quotes
removePunctuation= ", . ? : ; \" \' \' --"

#### change these lists as you wish ####
########################################

coolLettersList = coolLetters.split(' ')
removePunctuationList = removePunctuation.split(' ')

# open file and make it into a long string
with open('source-text.txt', 'r') as inputfile:
    words=inputfile.read().replace('\n', ' ')

# split string into list
wordsList = words.split(" ")

# make set (list of unique items) from list 
wordsSet = set(wordsList)

# remove punctuation from words set
cleanWordsSet = []
for word in wordsSet:
    for glyph in word:
        if glyph in removePunctuationList:
            word = word.replace(glyph,'x')
    # add to "clean" list
    cleanWordsSet.append(word)

# make list of only cool words (words containing characters in coolLetters)

coolWordsSet = []
coolWord = False
for word in cleanWordsSet:
    for glyph in word:
        if glyph in coolLettersList:
            coolWord = True
        else:
            coolWord = False
    if coolWord == True:
        print(word)
        coolWordsSet.append(word)

coolWords= open("cool-words.txt","w+")

for word in coolWordsSet:
    coolWords.write(f'{word} \n')

coolWords.close()