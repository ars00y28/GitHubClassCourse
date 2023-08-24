

num = 10
for m in range(num):
    for n in range(num-m):
        print(' ',end='')
    for o in range(m+1):
        print('*',end='')
    print()
    