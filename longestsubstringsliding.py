s="abkdgbcsiugkj"
n=len(s)
l=0
r=0
maxlen=0
visited=set()
while r<n:
    if s[r] not in visited:
        visited.add(s[r])
        len=r-l+1
        r+=1
    else:
        visited.remove(s[l])
        l+=1
    maxlen=max(maxlen,len)
print(maxlen)