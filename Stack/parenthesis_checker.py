# paranthesis check





#User function Template for python3

class Solution:

    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        # code here

        st = []


        for i in x:

            if i in ["(", "[", "{"]:
                st.append(i)

            else:

                if len(st)<= 0:
                    return False

                elif i == ")":
                    ch = st.pop()
                    if ch!= "(":
                        return False
                elif i == "}":
                    ch = st.pop()
                    if ch!= "{":
                        return False
                elif i== "]":
                    ch = st.pop()
                    if ch != "[":
                        return False


        if len(st)>0:
            return False
        return True

