class Solution:
    
    def is_valid(self, st):
        
        ips = st.split(".")
        
        for i in ips:
            if len(i) > 3 or int(i) < 0 or int(i) > 255:
                return False
                
            if len(i)>1 and int(i) == 0:
                return False
                
            if len(i) > 1 and int(i) != 0 and i[0] == "0":
                return False
        return True
    
    def genIp(self, s):
        #Code here
        
        st = s
        n = len(s)
        
        if n > 12:
            return []
        
        ans = []
        
        for i in range(1, n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    
                    st = st[:k] +"."+ st[k:]
                    st = st[:j] +"."+ st[j:]
                    st = st[:i] +"."+ st[i:]
            
                    if self.is_valid(st):
                        ans.append(st)
                    
                    st = s
    
        return ans
