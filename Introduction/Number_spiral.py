for _ in range(int(input())):
    n,m=map(int,input().split())
    mx=max(n,m)-1
    mn=mx**2+1
    mx=(mx+1)**2
    print(mn,mx)