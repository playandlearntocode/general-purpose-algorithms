class Solution:
    MIN_INT = pow(-2, 31)
    MAX_INT = pow(2, 31) - 1

    def recursiveDivide(self, currentDividend: int, currentDivisor: int):
        quotient = 1
        accumulator = currentDivisor  # same as currentDivisor * quotient because quotient == 1 at this point
        # base case
        if currentDividend < currentDivisor:
            return 0
        elif currentDividend == currentDivisor:
            return 1

        while accumulator < currentDividend:
            quotient = quotient << 1
            accumulator = accumulator << 1  # implicit quotient inclusion here!

        # undo the last step, because accumulator is now larger than currentDividend
        accumulator = accumulator >> 1
        quotient = quotient >> 1
        return quotient + self.recursiveDivide(currentDividend - accumulator, currentDivisor)

    def divide(self, dividend: int, divisor: int) -> int:
        # determine the sign of quotient:
        negative = False
        if (dividend >= 0 and divisor >= 0):
            negative = False
        elif (dividend < 0 and divisor >= 0):
            negative = True
        elif (dividend > 0 and divisor <= 0):
            negative = True

        # extract positive values of dividend and divisor:
        absDividend, absDivisor = abs(dividend), abs(divisor)

        # watch for limits:
        if (absDivisor == 1):
            if (negative == True):
                return -absDividend if Solution.MIN_INT < -absDividend else Solution.MIN_INT
            else:
                return absDividend if Solution.MAX_INT > absDividend else Solution.MAX_INT

        q = self.recursiveDivide(absDividend, absDivisor)
        return q if negative == False else -q
