#!/usr/bin/env python
# Stephen Olsen
# LargeNumber class for SE final project
# Implemented with bytearrays
import operator
import random
import math

class LargeNumber:
    # Stores the number as an list of ints in base 10
    def __init__(self, number):
        if type(number).__name__=='list':
            self.num = number
        else:
            self.num = [int(char) for char in number]

    def __str__(self):
        return "".join([str(num) for num in self.num])

    # two helper functions, lineup and regulate
    def _lineup(self, num1, num2):
        if len(num1) > len(num2):
            num2 = [0 for i in range (len(num1) - len(num2))] + num2
        elif len(num1) < len(num2):
            num1 = [0 for i in range (len(num2) - len(num1))] + num1
        return num1, num2

    def _regulate(self, lst):
        count = 0
        for i in range(len(lst))[::-1]:
            lst[i] += count
            count = 0
            while lst[i] >= 10:
                lst[i] -= 10
                count += 1
        if count > 0:
            lst = [count] + lst
        return lst
    
    def __lt__(self, other):
        a, b = self._lineup(self.num, other.num)
        for i in range(len(a)):
            if a[i] < b[i]:
                return True
            if a[i] > b[i]:
                return False
        return False

    def __gt__(self, other):
        a, b = self._lineup(self.num, other.num)
        for i in range(len(a)):
            if a[i] > b[i]:
                return True
            if a[i] < b[i]:
                return False
        return False

    def __eq__(self, other):
        a, b = self._lineup(self.num, other.num)
        return reduce(operator.and_, [a[i] == b[i] for i in range(len(a))])

    def __add__(self, other):
        a, b = self._lineup(self.num, other.num)
        total = [a[i] + b[i] for i in range(len(a))]
        carry = 0
        for i in range(len(a))[::-1]:
            total[i] += carry
            if total[i] > 9:
                old = total[i]
                total[i] = old % 10
                carry = old / 10
            else:
                carry = 0
        while carry != 0:
            total = [carry % 10] + total
            carry = carry / 10
        return LargeNumber(total)

    def __sub__(self, other):
        if self < other:
            raise(Exception("fail"))
        a, b = self._lineup(self.num, other.num)
        answer = [0] * len(a)
        borrowed = False
        for i in range(len(a))[::-1]:
            if borrowed:
                a[i] -= 1
            if a[i] < b[i]:
                a[i] += 10
                borrowed = True
            else:
                borrowed = False
            answer[i] = a[i] - b[i]
        # Strip Away Leading 0's
        while answer[0] == 0:
            if len(answer) > 0:
                answer = answer[1:]
            else:
                answer = [0]
                break
        
        return LargeNumber(answer)

    def __mul__(self, other):
        a, b = self._lineup(self.num, other.num)
        rows = [map(lambda x:x*i,a) for i in b[::-1]]
        rows = map(self._regulate, rows)
        offset_rows = [ rows[i] + (i*[0]) for i in range(len(rows))]
        offset_rows = map(lambda x:LargeNumber("".join(
            map(lambda y: str(y), x))), offset_rows)
        answer = reduce(operator.add, offset_rows)
        return answer

    def __div__(self, other):
        quotent, remainder = self._divide(other)
        return quotent

    def __mod__(self, other):
        quotent, remainder = self._divide(other)
        return remainder

    def _divide(self, other):
        sub = LargeNumber(self.num[:len(other.num)])
        digits = len(other.num)
        if sub < other:
            digits += 1
        a, b = self.num, other.num
        answer = []
        count = 0

        dividend = a[:digits - 1]
        for place in range(digits - 1, len(a)):
            dividend = dividend + [a[place]]
            count = 0
            sub = dividend
            Lsub = LargeNumber(sub)
            Lb   = LargeNumber(b)
            while Lsub > Lb:
                Lsub -= Lb
                count += 1
            answer = answer + [count]
            dividend = Lsub.num
        remainder = LargeNumber(dividend)
        return LargeNumber(answer), remainder

    def __rshift__(self, other):
        answer = int(self.__str__()) >> int(other.__str__())
        return LargeNumber(str(answer))

    def __and__(self, other):
        answer = int(self.__str__()) & int(other.__str__())
        return LargeNumber(str(answer))

    def __trunc__(self):
        return (int(self.__str__()))

    def Random(num1, num2):
        r = random.randrange(int(str(num1)), int(str(num2)))
        return LargeNumber(str(r))
