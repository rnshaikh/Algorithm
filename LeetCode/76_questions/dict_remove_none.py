
ans = {}

def recur(d, key, ans, prev):
    
    if d[key] == None:
        return
    if type(d[key]) == dict:
        ans[key] = {}
        for k in d[key]:
            recur(d[key], k, ans, key)
    else:
        if prev:
            ans[prev][key] = d[key]
        else:
            ans[key] = d[key]

def process(d):
    ans = {}
    for key in d:
        recur(d, key, ans, None)
    return ans

asd = {
    "a": 1,
    "b": 2,
    "c": {
        "d" : 3,
        "e" : 4,
        "f" : None
    },
    "g": 6,
    "h": 7,
    "i": None,
    "k": {
        "l": None
    }
}

print(process(asd))


def process(a):
    
    n = len(a)
    i = 0
    j = i+1
    while j < n:
        if a[i] == 1 and a[j]!= 1:
            a[i], a[j] = a[j], a[i]
            i = i+1
        j = j+1
    return a


a = [1, 2, 3, 4, 5, 1,1,1,8,9,1,10]
print("process", process(a))
