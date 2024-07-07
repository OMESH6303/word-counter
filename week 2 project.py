
       # Text Analyzer Tool

def count_words(text):
    words = text.split()
    return len(words)

def count_specific_word(text, word):
    words = text.split()
    return words.count(word)

def analyze_text(text):
    word_count = count_words(text)
    print(f"Total words: {word_count}")
    
    specific_word = input("Enter a word to count its occurrences: ")
    word_frequency = count_specific_word(text, specific_word)
    print(f"Occurrences of '{specific_word}': {word_frequency}")

# Example text for analysis
example_text = "Python is a versatile programming language. It is used for web development, data analysis, automation, and much more."

# Running the text analyzer
analyze_text(example_text)
