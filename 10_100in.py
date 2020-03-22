f = open('output.txt')
l = f.readlines()
f.close()

data = []
for i in range(0, 101):
    data.append(int(l[i]))
    a = int(l[i]) ** 2
    print(a)