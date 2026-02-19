#  find longest world in a string

str = "Python is a great programming language"
words = str.split()
longest_word = max(words, key=len)
print("longest word in string is: ",longest_word)