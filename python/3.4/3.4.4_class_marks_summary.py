count = 0
mathSum, physSum, rusSum = 0, 0, 0
with open('dataset_3363_4.txt', 'r') as inf:
    for line in inf:
        count += 1
        name, mathStr, physStr, rusStr = line.split(';')
        math, phys, rus = float(mathStr), float(physStr), float(rusStr)
        print((math + phys + rus) / 3)
        mathSum += math
        physSum += phys
        rusSum += rus

print(str(mathSum / count) + ' ' +
      str(physSum / count) + ' ' + str(rusSum / count))
