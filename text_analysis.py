#Taking input from user
user_input = input('Enter a string: ')
user_input.lower()
print(user_input)

print('---- Text Analysis ----')

# Character count
character_count = 0
for words in user_input:
    for char in words:
        character_count += 1

print(f'total characters: {character_count}')

# word count
word_list = user_input.split()
print(f'total words: {len(word_list)}')

# vowel count
vowels = ['a', 'e', 'i', 'o', 'u']
vowel_count = 0
for vowel in vowels:
    if vowel in user_input:
        vowel_count += 1
print(f'total vowels: {vowel_count}')

# consonant count
consonants = [
    'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
    'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
consonant_count = 0
for consonant in consonants:
    if consonant in user_input:
        consonant_count += 1
print(f'total consonants: {consonant_count}')

# palindrome analysis
palindromes = []
reversed_input = user_input[::-1]
for i in reversed_input.split():
    for j in user_input.split():
        if i == j:
            palindromes.append(i)
print(f'palindromes: {palindromes}')

# reversed sentence
print(f'reversed sentence: {reversed_input}')


    
