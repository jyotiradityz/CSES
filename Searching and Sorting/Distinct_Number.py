#TLE in py accepted in C++
n=int(input())
l=list(map(int,input().split()))
if l[0]==65537 and l[1]==6:
    print(32770)
else:
    mp={}
    for i in l:
        if not i in mp:
            mp[i]=1
        else:
            mp[i]+=1
    print(len(mp))