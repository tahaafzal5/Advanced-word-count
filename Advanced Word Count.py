# analysis
# user needs to count the words in a file, excluding stop words

# specification
# user inputs a file
# stop words are not counted, all other unique words are counted
# output of the most used words in order of frequency

# design
# user inputs a file, which is opened as read
# the characters are replaced with spaces after making all text lowercase
# stopWordsEng file is also opened and the words from ti.txt are compared with stopWords
# unique words are counted and displayed in order of frequency

# returns the count and not the key
def byFreq(pair):
    return pair[1]


def main():

    # introduction
    print("This program analyzes word frequency in a file")
    print("and prints a report on the n most frequent words. \n")

    #get the sequence of words from the file
    fileName = input("File to analyze: ")
    text = open(fileName, "r").read()

    text = text.lower()

    # replaces all punctuation
    for aCharacter in '`-=\][;/.,~!@#$%^&*(:)_+"}{|?><':
        text = text.replace(aCharacter, " ")

    words = text.split()

    file = open("stopWordsEng.txt", "r").read()
    stopWords = file.split()

    # constructs a dictionary of word counts
    counts = {}
    for aWord in words:
        # compares every word in the text file to stopWords and counts if it is not a stopWord
        if aWord not in stopWords:
            counts[aWord] = counts.get(aWord, 0) + 1

    # output analysis of n most frequent words
    n = eval(input("Output analysis of how many words? "))
    items = list(counts.items())
    items.sort()
    items.sort(key = byFreq, reverse= True)

    # output
    for i in range(n):
        word, count = items[i]
        print("{0:<15}{1:>5}".format(word, count))

main()
