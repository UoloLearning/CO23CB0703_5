def count_vowels_and_consonants(word):
    """This function counts the number of vowels and consonants in a word."""
    num_vowels = 0
    num_consonants = 0
    for letter in word:
        if letter.lower() == 'a' or letter.lower() == 'e' or letter.lower() == 'i' or letter.lower() == 'o' or letter.lower() == 'u':
            num_vowels += 1
        else:
            num_consonants += 1
    return num_vowels, num_consonants

# Call the count_vowels_and_consonants function with an argument of "hello"
vowels, consonents = count_vowels_and_consonants("abcdefghijklmnopqrstuvwxyz")

# Print the result
print("Number of vowels:", vowels)
print("Number of consonants:", consonents)
