# Alternate positive and negative numbers


"""
    Method 1:

        initiate outofPlace = -1

        travers array :

            if coutplace == -1:
            check if current element is out place . ex odd index element is pos and even index element is negative
            if it is true outplace = current_index

            check if outplace >= 0
                then check if current element is corrent element ex if current element is pos if out place element is negative
                and current element is neg if outplace is postive
                then rotate_right(arr, outplace, cur) rotate right element between current element and outplace element

                check if index-outplace>2:
                    outplace += 2
                else:
                    outplace = -1



    Method:2

        postive_arr = []
        negative_arr []

        traverse arr store positive_ele in positive_arr
        and negative_ele in negative_arr

        postive_index = 0
        negative_index = 0
        i=0

        while i < n:

            if i is even:
                if i is less than len(positive_arr)-1:
                    arr[i] = positive_arr[positive_index]
                    positive_index = positive_index + 1
                else:
                    arr[i] = neg_arr[neg_index]
                    neg_index = neg_index + 1

            if i is odd:
                if i is less than len(negative_arr)-1:
                    arr[i] = negative_arr[neg_index]
                    neg_index = neg_index+1
                else:
                    arr[i] = pos_arr[pos_index]
                    pos_index = pos_index + 1




"""


class Solution:

    # def rightRotate(self, arr, n, outOfPlace, cur):
    #     temp = arr[cur]
    #     for i in range(cur, outOfPlace, -1):
    #         arr[i] = arr[i - 1]
    #     arr[outOfPlace] = temp
    #     return arr



    def rearrange(self,arr, n):
        # code here

        # outOfPlace = -1
        # for index in range(n):
        #     if(outOfPlace >= 0):

        #         # if element at outOfPlace place in
        #         # negative and if element at index
        #         # is positive we can rotate the
        #         # array to right or if element
        #         # at outOfPlace place in positive and
        #         # if element at index is negative we
        #         # can rotate the array to right
        #         if((arr[index] >= 0 and arr[outOfPlace] < 0) or
        #           (arr[index] < 0 and arr[outOfPlace] >= 0)):
        #             arr = self.rightRotate(arr, n, outOfPlace, index)
        #             if(index-outOfPlace > 2):
        #                 outOfPlace += 2
        #             else:
        #                 outOfPlace = - 1

        #     if(outOfPlace == -1):

        #         # conditions for A[index] to
        #         # be in out of place
        #         if((arr[index] < 0 and index % 2 == 0) or
        #           (arr[index] >= 0 and index % 2 == 1)):
        #             outOfPlace = index

        # return arr

        positive_arr = []
        negative_arr = []

        for i in range(n):
            if arr[i]>=0:
                positive_arr.append(arr[i])
            else:
                negative_arr.append(arr[i])

        i=0
        pos_index = 0
        neg_index = 0

        while i < n:

            if i%2 == 0 :
                if(pos_index<=(len(positive_arr)-1)):
                    arr[i] = positive_arr[pos_index]
                    pos_index += 1
                else:
                    arr[i] = negative_arr[neg_index]
                    neg_index += 1


            elif i%2 == 1:

                if(neg_index <= (len(negative_arr)-1)):
                    arr[i] = negative_arr[neg_index]
                    neg_index += 1
                else:
                    arr[i] = positive_arr[pos_index]
                    pos_index += 1

            i = i+1

