sentence = "Nature is the ultimate masterpiece,calm yet powerful, simple yet complex. From towering mountains to tiny dewdrops, every part has a role."
wordcount = {}
for word in sentence.split():
    wordcount[word] = wordcount.get(word, 0) + 1
print (wordcount)
