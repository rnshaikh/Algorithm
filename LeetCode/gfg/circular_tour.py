"""
Suppose there is a circle. There are N petrol pumps on that circle. You will be given two sets of data.
1. The amount of petrol that every petrol pump has.
2. Distance from that petrol pump to the next petrol pump.
Find a starting point where the truck can start to get through the complete circle without exhausting its petrol in between.
Note :  Assume for 1 litre petrol, the truck can go 1 unit of distance.

Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

"""

"""
    take start=0,
    extra_fuel=0 for storing fuel after subtracting current distance
    required_fuel= 0 if some point fuel is less then stored that fuel so that after traversing
                     array we can check if extra_fuel is greater than equal to required_fuel return than start

    traverse array from 0:
        caluclate extrafuel += arr[i][0] - arr[i][1]

        if extra_fuel < 0:
            updated required_fuel += extra_fuel
            start = i+1 increment by 1
            extra_fuel = 0


    if extra_fuel>= required_fuel: return start
    else:
        return -2




"""



{'AECO': 5, 'HOUSTON': 4, 'JCPL': 6, 'NORTH': 1, 'PSEG': 7, 'SOUTH': 2, 'WEST': 3}  
{'RT': 1, 'DA': 2}

class Solution:

    #Function to find starting point where the truck can start to get through
    #the complete circle without exhausting its petrol in between.
    def tour(self,lis, n):
        #Code here

        start = 0
        required_fuel = 0
        extra_fuel = 0

        for i in range(n):

            extra_fuel = extra_fuel + (lis[i][0] - lis[i][1])

            if(extra_fuel < 0):
                required_fuel = required_fuel + extra_fuel
                start = i+1
                extra_fuel = 0


        #print("extra , required", extra_fuel, required_fuel)
        if(extra_fuel >= abs(required_fuel)):
            return start
        else:
            return -1
