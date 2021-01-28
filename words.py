def print_upper_words(input, must_start_with={}):
    """print out the provided list of words in uppercase
    if optional starting letters given, limit to words that start with those letters"""
    for word in input:
        if word[0] in must_start_with:
            print(word.upper())
    
print_upper_words(['hello', 'hey', 'goodbye', 'yo', 'yes'], must_start_with={'h', 'y'})