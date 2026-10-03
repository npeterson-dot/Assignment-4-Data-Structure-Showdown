# Timed Challenge: Unique Word Count
# Write a function that takes a list of words and returns the number
# of unique words in the list.


def unique_word_count(words):
    if not isinstance(words, list):
        return 0

    unique_words = set(words)
    return len(unique_words)


# Test 1: Normal list with duplicates
print(unique_word_count(["apple", "banana", "apple", "orange"]))
# Expected: 3

# Test 2: All unique words
print(unique_word_count(["red", "blue", "green"]))
# Expected: 3

# Test 3: Empty list
print(unique_word_count([]))
# Expected: 0

# Test 4: All duplicate words
print(unique_word_count(["hello", "hello", "hello"]))
# Expected: 1

# Test 5: Wrong data type
print(unique_word_count("apple"))
# Expected: 0