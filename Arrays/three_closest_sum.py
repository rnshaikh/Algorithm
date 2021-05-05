
## three closest sum

"""
    method:1  two pointer method

    1) intialize array l =[]
    2) sort array
    3) traverse element of array
    4) initalize j = 0 and k=len(arr)-1
    5) if j is less than k and i is not j and i is not k
    6) add p = current[i] + arr[j] + arr[k]
    7) if  p == target then return p
    8) if p less than target  then  l.append(p) ; j = j+1
    9) else l.append(p); k = k-1
    10) sort array in descending order
    11) d = abs(target-l[0])
    12) res = l[0]
    13) traverse each element in l ; y = abs(i-target)  if y<d: d=y; res=i
    14) resturn res

"""


class Solution:
    def threeSumClosest(self, arr, x) :

        l=[]
        arr.sort()
        for i in range(len(arr)):
            j=0
            k=len(arr)-1
            while(j<k and i!=j and i!=k):
                p=arr[i]+arr[j]+arr[k]
                if p==target:
                    return p
                elif p<target:
                    l.append(p)
                    j+=1
                else:
                    l.append(p)
                    k-=1

        l.sort(reverse=True)
        d=abs(target-l[0])
        res=l[0]
        for i in l:
            y=abs(i-target)
            if y<d:
                d=y
                res=i
        return res
