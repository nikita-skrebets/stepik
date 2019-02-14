numClasses = 11
def init(classHeights):
    for i in range(1, numClasses + 1):
        classHeights[i] = []

classHeights = {}
init(classHeights)

with open('dataset_3380_5.txt', 'r') as inf:
    for line in inf:
        (cl, n, h) = line.split('\t')
        classHeights[int(cl)].append(int(h))

for i in range(1, numClasses + 1):
    if len(classHeights[i]) == 0:
        print(i, '-')
        continue
    print(i, sum(classHeights[i])/len(classHeights[i]))
