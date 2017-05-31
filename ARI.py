import sys

def numWords(text):
    #returns number of words in text file

    word_list = text.split()
    return len(word_list)

def numSentences(text):
    #returns number of sentences in text file

    word_list = text.split()
    sentences = [word.count(".") for word in word_list]
    return sum(sentences)

def numChars(text):
    #return number of character in text file
    word_list = text.split()
    char_list = [len(w) for w in word_list]
    return sum(char_list)

def avgLetters(text):
    #returns average number of letters per 100 words in a text file
    #uses a list of 100 word chunks to calculate this

    word_list = text.split()
    intervals = range(0, len(word_list), 100)
    word_chunks = [word_list[n:n+100] for n in intervals]
    lettersList = []
    for n in range(0, len(intervals)):
        words = [len(i) for i in word_chunks[n]]
        letters = sum(words)
        lettersList.extend([letters])
    L = sum(lettersList)
    return float(L/len(word_chunks))

def avgSentences(text):
    #takes entire text and returns average number of sentences per 100 words
    word_list = text.split()
    intervals = range(0, len(word_list), 100)
    word_chunks = [word_list[n:n+100] for n in intervals]
    sentencesList = []
    for n in range(0,len(intervals)):
        sentences = [word.count(".") for word in word_chunks[n]]
        total = sum(sentences)
        sentencesList.extend([total])
    S = sum(sentencesList)
    return float(S/len(word_chunks))

def sortAlgo(algo, text):
    #takes in an algorithm type and text and prints a readability index
    if sys.argv[1] == "ARI":
        num_char = float(numChars(text))
        num_words = float(numWords(text))
        num_sentences = float(numSentences(text))
        ARI = (4.71 * (num_char/num_words)) + (0.5 * (num_words/num_sentences)) - 21.43
        print ARI
    elif sys.argv[1] == "Coleman-Liau":
        L = avgLetters(text)
        S = avgSentences(text)
        index = float((0.0588*L)-(.296*S) - 15.8)
        print index
    else:
        print ('Sorry algorithm not recognized. Type "ARI or "Coleman-Liau"')

def main():
    filename = sys.argv[2]
    with open(filename, 'r') as input_file:
        text = input_file.read()
    sortAlgo(sys.argv[1], text)



if __name__ == "__main__":
    main()
