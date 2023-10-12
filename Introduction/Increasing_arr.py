n=int(input())
l=list(map(int,input().split()))
ans=0
for i in range(len(l)-1):
    if l[i+1]<l[i]:
        ans+=l[i]-l[i+1]
        l[i+1]=l[i]
print(ans)