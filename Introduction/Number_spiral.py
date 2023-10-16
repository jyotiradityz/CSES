for _ in range(int(input())):
    n,m=map(int,input().split())
    mx=max(n,m)-1
    mn=mx**2+1
    mx=(mx+1)**2
    ans=0
    if max(n,m)%2==0:
        ans=mn+min(m,n)-1
    else:
        ans=mx-min(n,m)-1   
    print(ans)