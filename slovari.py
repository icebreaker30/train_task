fil = open('input.txt')
for line in fil:
    list1 = line.split(' ')
    mdc = dict()
    for i in list1:
        if i in mdc:
            mdc[i] = mdc.get(i, 0) + 1
        else:
            mdc[i] = 1
        print(mdc[i]-1, end=' ')
