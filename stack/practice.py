from collections import deque

class stack:
    def __init__(self):
        self.s = deque()

    def push(self, data):
        self.s.append(data)

    def pop(self):
        return self.s.pop()

    def peek(self):
        return self.s[-1]    

    def is_empty(self):
        return len(self.s) == 0

    def size(self):
        return len(self.s)    

    def reverse_string(self, s):
        for i in s:
            self.push(i)
        newS = ''    
        for i in s:
            newS += self.pop()
        print(newS)    

    def is_balanced(self, s):
        d = {"}" : "{", "]" : "[", ")" : "("}
        for i in s:
            if i == "{" or i == "(" or i == "[":
                self.push(i)
            if i == "}" or i == ")" or i == "]":
                if self.size() == 0:
                    return False
                if self.pop() != d[i]:
                    return False
        return self.is_empty()          

st = stack()
st.reverse_string("We will conquere COVID-19")
print(st.is_balanced("({a+b})"))   
print(st.is_balanced("))((a+b}{"))   
print(st.is_balanced("((a+b))"))   
print(st.is_balanced("))"))          
print(st.is_balanced("[a+b]*(x+2y)*{gg+kk}"))
