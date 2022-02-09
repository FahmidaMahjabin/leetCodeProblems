# function = reverse an integer number 
# step1: number k 10 diye devide kore er remainder k ekta variable e rakhbo string hishebe 
# step2: resultant k abar 10 diye vag kore remainder k string concate korbo 
# step3:resultant 0 na howa porjnoto korbo 
class Solution:
    def reverse(self, number: int) -> int:
        reverseNumber = 0
        if number < 0:
            multiplier = -1
            number = multiplier * number
        else:
            multiplier = 1
        while number >0:
            remainder = number % 10
            reverseNumber = reverseNumber *10 + remainder
            number = number // 10
        reverseNumber = multiplier * reverseNumber
        if reverseNumber <= -2**31 or reverseNumber >= 2**31 -1:
            return 0
        return reverseNumber

print(-123 % 10)
number= 2147483647
print(number.bit_length())