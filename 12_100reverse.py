f = open('output.txt')
l = f.readlines()
f.close()

for i in reversed(range(0, 101)):
    a = int(l[i]) * 2
    print(a) 
