# cypher keys and values
cKeys = input()
cValues = input()

# populate cypher and decypher
cypher, decypher = {}, {}
for i in range(len(cKeys)):
    cypher[cKeys[i]] = cValues[i]
    decypher[cValues[i]] = cKeys[i]

strToCypher = input()
strToDecypher = input()

cyphered = ''
for l in strToCypher:
    cyphered += cypher[l]

print(cyphered)

decyphered = ''
for l in strToDecypher:
    decyphered += decypher[l]

print(decyphered)
