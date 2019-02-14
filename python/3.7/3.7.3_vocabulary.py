def getDict(dict):
    cnt = int(input())
    for i in range(cnt):
        knownWords.add(input().lower())

def getUnknownWords(knownWords):
    unknownWords = set()
    cnt = int(input())
    for i in range(cnt):
        for w in input().split(' '):
            if w.lower() not in knownWords:
                unknownWords.add(w)
    return unknownWords


knownWords = set()
getDict(knownWords)

for w in getUnknownWords(knownWords):
    print(w)
