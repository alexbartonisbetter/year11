words = {}
sentence = input("enter a sentence: ")
sentence = sentence.lower()
word_list = sentence.split(" ")
for word in word_list:
    if word in words:
        words[word] += 1
    else:
        words[word] = 1
for k, v in words.items():
    print(k , v)