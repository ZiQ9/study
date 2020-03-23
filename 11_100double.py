f = open('output.txt')
l = f.readlines()
f.close()

for i in range(0, 101):
    print(int(l[i]),int(l[i]))
