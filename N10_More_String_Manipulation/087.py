words = []
word = input("Enter a word: \n")
for i in word:
    words.append(i)
words.reverse()
for i in words:
    print(i)