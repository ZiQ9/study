f = open('output.txt')
l = f.readlines()
f.close()

data = []
for i in reversed(range(0, 101)):
    data.append(int(l[i]))
    print(int(l[i]))