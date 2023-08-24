def prime(num:int)->bool:
    prime = True
    i = 2 
    if num == 1:
        prime = None
    elif num == 2:
        prime = True
    elif num <= 0 : 
        prime = None
    else:
        for i in range(2,num):
            if num % i == 0 :
                prime = False

            break
    return prime

n = int(input('Enter a number'))
res = prime(n)
if res == True:
    print('Prime number')
else:
    print('Not prime')



