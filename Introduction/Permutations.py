n=int(input())
if n<=3 and n!=1:
    print('NO SOLUTION')
elif n==4:
    print('2 4 1 3')
else:
    if n&1:
        for i in range(1,n//2+1):
            print(i,i+n//2+1,end=' ')
        print(n//2+1)
    else:
        for i in range(1,n//2+1):
            print(i,i+n//2,end=' ')
            
    