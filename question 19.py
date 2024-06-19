def remove_punctuation(input_string):
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    result = ""
    
    for char in input_string:
        if char not in punctuation:
            result += char
    return result

# Test cases
test_string1 = "Hello, world! How's it going?"
test_string2 = "Python's syntax is clean & simple."

print(f'Original: {test_string1}')
print(f'Without punctuation: {remove_punctuation(test_string1)}')

print(f'Original: {test_string2}')
print(f'Without punctuation: {remove_punctuation(test_string2)}')
