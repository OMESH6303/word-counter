def word_count(text):
    """
    Function to count the number of words in a given text.
    """
    words = text.split()
    return len(words)

def main():
    """
    Main function to handle user input, call word_count function, and display the result.
    """
    print("Welcome to Word Counter!")
    print("Please enter a sentence or paragraph:")
    
    # Taking user input
    user_input = input()
    
    # Checking if input is empty
    if not user_input.strip():
        print("Error: Input is empty.")
    else:
        # Counting words
        count = word_count(user_input)
        print(f"Word count: {count}")

if __name__ == "__main__":
    main()
