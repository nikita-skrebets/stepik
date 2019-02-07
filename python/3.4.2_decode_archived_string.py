with open('dataset_3363_2.txt', 'r') as inf:
    coded = inf.readline().strip()

uncoded = ''
i = 0
while i < len(coded):
    letter = coded[i]

    i += 1
    countStr = ''
    while i < len(coded) and coded[i].isdigit():
        countStr += coded[i]
        i += 1

    count = int(countStr)
    uncoded += letter * count

print(uncoded)
