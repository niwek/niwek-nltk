import nltk

def test_nltk():
    sentence = """At eight o'clock on Thursday mornin\ngArthur didn't feel very good."""
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    print(tagged)

def main():
    test_nltk()

if __name__ == "__main__":
    main()