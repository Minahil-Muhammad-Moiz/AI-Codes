#  TASK 01 Program to remove punctuations from string.

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

string = '"Hey!! How are you?,"  I asked.'
new_string = ""
for char in string:
   if char not in punctuations:
       new_string += char

print("Original String: ", string)
print('String With Removed Punctuation: ', new_string)


# TASK 02 - Program to sort letters in words of a string.

string = 'hello this is python'
print('Sorted letters of each word: ', end='')
words = string.split()
for word in words:
    sorted_word = sorted(word)
    print(''.join(sorted_word), end=' ')

# TASK 03 - A program that converts text to speech or speech to text (optional)

import pyttsx3

txt_speech = pyttsx3.init()
text  = input('Enter the text you want to convert in speech ')
txt_speech.say(text)
txt_speech.runAndWait()