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

    return len(text)

def avgLetters(text):
    #returns average number of letters per 100 words in a text file
    #uses multiple lists to calculate this

    word_list = text.split()
    intervals = range(0, len(word_list), 100)
    word_chunks = [word_list[n:n+100] for n in intervals]
    lettersList = []
    for n in range(0, len(intervals)):
        words = [len(i) for i in word_chunks[n]]
        letters = sum(words)/10
        lettersList.extend([letters])
    L = sum(lettersList)
    return L/len(word_chunks)

def main():
    filename = sys.argv[2]
    with open(filename, 'r') as input_file:
        text = input_file.read()
    if sys.argv[1] == "ARI":
        num_char = numChars(text)
        num_words = numWords(text)
        num_sentences = numSentences(text)
        ARI = 4.71*(num_char/num_words)+ (.5*(num_words/num_sentences)-21.43)
        print ARI
    elif sys.argv[1] == "Coleman-Liau":
        L = avgLetters(text)
        #TODO make function to find avg number of sentences
    else:
        pass


if __name__ == "__main__":
    main()
