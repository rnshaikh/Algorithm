"""
There are buckets buckets of liquid, where exactly one of the buckets is poisonous. To figure out which one is poisonous, 
you feed some number of (poor) pigs the liquid to see whether they will die or not. 
Unfortunately, you only have minutesToTest minutes to determine which bucket is poisonous.

You can feed the pigs according to these steps:

Choose some live pigs to feed.
For each pig, choose which buckets to feed it. The pig will consume all the chosen buckets simultaneously and will take no time.
Wait for minutesToDie minutes. You may not feed any other pigs during this time.
After minutesToDie minutes have passed, any pigs that have been fed the poisonous bucket will die, and all others will survive.
Repeat this process until you run out of time.
Given buckets, minutesToDie, and minutesToTest, 
return the minimum number of pigs needed to figure out which bucket is poisonous within the allotted time.

"""

"""

    let p = timegivenfortest  m = timerequiredtodie   n = no_of bucket

    no_round = (P//M) + 1


    x^no_round = no_of_bucket

    taking log on both side
    log x = log(no_of_bucket) / log(no_round)

    x = log(no_of_bucket) / log(no_round)


"""





import math
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:


        no_round = (minutesToTest // minutesToDie) + 1


        no_of_pig = math.ceil(math.log(buckets) / math.log(no_round))

        return no_of_pig
