from random import choice
import sys

def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file_string = open(file_path).read()

    return file_string


def make_chains(text_string, n=2):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """
    chains = {}
    words = text_string.split()

    wordtup = tuple()
    for i in range(len(words)-n):
        for z in range(i, i+n):
            wordtup = wordtup + (words[z],)

        chains[wordtup] = chains.get(wordtup, list()) + [words[i+n]]
        wordtup = tuple()

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    tup_word = choice(chains.keys())
    text += str(tup_word[0]) + " " + str(tup_word[1])
    word1 = tup_word[1]
    word2 = choice(chains[tup_word])
    text += " " + word2

    while True:
        tup_word = (word1, word2)
        if tup_word in chains:
            word1 = tup_word[1]
            word2 = choice(chains[tup_word])
            text += " " + word2
        else:
            break

    return text


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
