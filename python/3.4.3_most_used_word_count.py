wordCount = {}
with open('dataset_3363_3.txt', 'r') as inf:
    for line in inf:
        for word in line.lower().split():
            if word in wordCount:
                wordCount[word] += 1
            else:
                wordCount[word] = 1

maxWord = ''
maxCount = 0
for word, count in wordCount.items():
    if count >= maxCount or count == maxCount and word < maxWord:
        maxWord, maxCount = word, count

print(maxWord, maxCount)
