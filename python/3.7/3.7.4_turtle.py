coord = [0, 0]
for i in range(int(input())):
    (nwes, cm) = input().split(' ')
    cm = int(cm)

    if nwes == 'север':
        coord[1] += cm
    elif nwes == 'юг':
        coord[1] -= cm
    elif nwes == 'восток':
        coord[0] += cm
    elif nwes == 'запад':
        coord[0] -= cm

print(coord[0], coord[1])
