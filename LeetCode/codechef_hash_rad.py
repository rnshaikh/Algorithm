"""
Radhesh is learning Hashing!! He has a string S consisting only of lowercase English alphabets. To each alphabet, he assigns a value, i.e. a is assigned 0, b is assigned 1, …, and z is assigned 25. Now, hash of a string S is sum of values of all of its characters.

Now Ms Geethakoomaree, his Cryptography teacher, says that the hash function is poor because there can be multiple strings with same hash value. Hence, given a string S, you need to find its hash and another string P of same length (which is not same as S) with same hash. In case multiple P exists, print the lexicographically smallest one. If no such string exists, print −1.

Input:
The first line has a single integer T, denoting number of test cases per file.
The only line of each testcase contains the string S

Sample Input:
2
abz
yzz

Sample Output:
26 acy
74 zyz

"""

def find_hash(s):
    hash_a = 0
    for i in s:
        num = ord(i) % ord('a')
        hash_a = hash_a + num
    return hash_a

def find_s(s):

    hash_a = find_hash(s)
    ans = ""
    n = len(s)
    an = hash_a

    while len(ans) < n:
        if an-25 > 0:
            an = an-25
            ans = ans + "z"
        else:
            ans = chr(an+97)+ans
            if an > 0:
                an = an - an

    if ans == s:
        flag = False
        if "z" not in ans:
            flag = True

        if not flag:
            for i in range(n-1, -1, -1):
                if ans[i] != 'z':
                    new_char = chr(ord(ans[i]) + 1)
                    rep_char = chr(24+97)
                    ans = ans[:i] +  new_char+ rep_char  + ans[i+2:]
                    break
        else:
            if len(ans)>1:
                new_char = chr(ord(ans[n-2]) + 1)
                rep_char = chr(ord(ans[n-1])-1)
                ans = ans[:-n-2] + new_char + rep_char

    print(hash_a,ans,sep=" ")

t = int(input())
while t>0:
    s = input()
    n = len(s)
    a_s = 'a' * n
    z_s = 'z' * n
    if len(s) == 1 or s in [a_s, z_s]:
        hash_a = find_hash(s)
        print(hash_a, -1, sep=" ")
    else:
        find_s(s)
    t = t-1


