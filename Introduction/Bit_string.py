n=int(input())
ans=1
for i in range(n):
    ans=(ans*2)%(10**9+7)
print(ans)