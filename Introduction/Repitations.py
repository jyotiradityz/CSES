l=input()
ans=-1
cnt=0
ch=l[0]
for i in l:
    # print(i)
    if  i==ch:
        cnt+=1
    else:
        ans=max(ans,cnt)
        cnt=1
        ch=i
print(max(cnt,ans))     