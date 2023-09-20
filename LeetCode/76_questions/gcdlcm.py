class Solution:
    
    def gcd(self, a, b):
        
        if b == 0:
            return a
            
        return self.gcd(b, a%b)
    
    
    def lcmAndGcd(self, A , B):
        # code here 
        
        gc = self.gcd(A, B)
        
        lcm = abs(A * B)
        lcm = lcm // gc
        
        arr = [lcm, gc]
        return arr
        
