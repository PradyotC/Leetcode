class Solution:
    def getSum(self, a: int, b: int) -> int:
        a1,b1 = abs(a),abs(b)
        a,b,a1,b1 = (a,b,a1,b1) if a1>b1 else (b,a,b1,a1)
        if a>=0:
            if b>=0: sign = 1
            else: sign = 0
        else:  sign = -1
        # print(a1,b1,sign)
        if sign:
            add = a1 ^ b1
            carry = (a1 & b1) << 1
            while carry:
                x = add ^ carry
                y = (add & carry) << 1
                add,carry = x,y
            return sign*add
        else:
            sub = a1 ^ b1
            borrow = (~a1 & b1) << 1
            while borrow:
                x = sub ^ borrow
                y = (~sub & borrow) << 1
                sub,borrow = x,y
            return sub