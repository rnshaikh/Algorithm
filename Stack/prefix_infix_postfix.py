"""
infix - operator comes in between oprand ex. (2*5)+(3*4)-9
prefix - operator comes before operand ex.  -+*25*349
postdfix - operatore comes after operand ex. 25*34*+9-
"""


"""
    evaluation of postfix expression:
    1) get stack
    2) whenver operand comes push into stack
    3) whenever operator comes pop 2 from stack apply oprator push result in to stack
    3) after expression finish. element in stack will be result


    evalution of prefix expression:
    1) get stack
    2) travers from right
    3) push whenver operand comes into stack
    4) whenver operator comes pop 2  from stack apply operator push in to stack
    5) after expression finish element in stack will be result

"""


"""
    infix to postfix expression conversion

    1) without parenthesis
    infix = 2+3*9

    1) take stack and s = ""
    2) traverse infix expression from left to right
    3) if it operand add to string s
    4) if it is operator check top of the stack has higher precedence if yes then pop add to string s
    5) push this current operator to stack
    6) traverse end pop remaining operator if any add to string s



    1) with parenthesis
    infix = 2+(3*9)

    1) take stack and s = ""
    2) traverse exp from left to right
    3) if it is operand add to a string
    3) if is is opening parenthesis push to stack
    4) if is is opeator check top of stack has higher priority than current if yes and until opening parenthesis in stack then pop of stack add to string s
    5) push this current operator on stack
    6) if its closing parentheisis pop operator from stack add to s until opening parenthesis and pop opening parenthisis from stack
    6) traverse end pop remaining operator and add to string s
"""
