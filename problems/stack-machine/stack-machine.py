class StackMachine():

    def __init__(self):
        self.digits = "0123456789"
        self.ops = "+*"
        self.stack = []

    def push(self, char):
        if char in self.ops:
            try:
                e1 = self.pop()
                e2 = self.pop()
                if char == "+":
                    self.stack.append(e1+e2)
                else:
                    self.stack.append(e1*e2)
                return
            except:
                # Illegal operation
                return -1
        elif char in self.digits:
            self.stack.append(int(char))
        else:
            # Illegal character
            return -1

    def pop(self):
        if not self.stack:
            return None
        return self.stack.pop()

def solution(string):
    sm = StackMachine()
    for char in string:
        sm.push(char)
    result = sm.pop()
    if not result:
        print -1
    else:
        print result

solution("13+62*7+*") # 76
solution("11++") # -1
