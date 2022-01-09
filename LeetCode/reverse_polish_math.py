"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

"""


class Solution:

    def is_operator(self, sto):
        if sto == "+" or sto =="-" or sto == "/" or sto == "*" :
            return True
        else:
            return False

    def evalRPN(self, tokens: List[str]) -> int:

        st = []
        st.append(tokens[0])
        for i in range(1, len(tokens)):
            if(self.is_operator(tokens[i])):
                num2= int(st.pop(-1))
                num1 = int(st.pop(-1))
                if tokens[i] == "+":
                    st.append(num1+num2)
                elif tokens[i] == "-":
                    st.append(num1-num2)
                elif tokens[i] == "*":
                    st.append(num1*num2)
                elif tokens[i] == "/":
                    st.append(num1/num2)
            else:
                st.append(tokens[i])

        return int(st[-1])
