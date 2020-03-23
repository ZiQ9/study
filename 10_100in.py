f = open('output.txt')
l = f.readlines()
f.close()

for i in range(0, 101):
    a = int(l[i]) ** 2
    print(a)
