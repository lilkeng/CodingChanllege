'''
Requirements for atoi:
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

'''
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        i = 0
        sign = 1
        res = 0
        length = len(str)
        maxInt = (1<<31)-1
        
        if str == '':
            return 0
        
        if str[i] == '+':
            i += 1
        elif str[i] == '-':
            i += 1
            sign = -1
            
        for i in range(i, length):
            if str[i]>='0' and str[i]<='9':
                res = res * 10 + int(str[i])
            #ignore the charaters after meet the non-numerical 
            else:
                break
            if res > maxInt:
                break
        res = res * sign
        if res > maxInt:
            return maxInt
        # can't get the minimum int, so create one
        elif res < maxInt * -1:
            return maxInt * -1 -1
            
        return res