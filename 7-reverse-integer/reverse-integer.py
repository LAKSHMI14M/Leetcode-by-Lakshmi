class Solution(object):
    def reverse(self, x):
       INT_MIN, INT_MAX = -2147483648, 2147483647
       # x.reverse() only for list
       # for string we can do [::-1]
       #for int we can do big proacess or num to str and str to reverse
       sign=-1 if x<0 else 1# terinary operator to ease of conditional operations
       x=x*sign
       string=str(x)[::-1]
       reversed_int=int(string)*sign
       if reversed_int < INT_MIN or reversed_int > INT_MAX:
            return 0
       return reversed_int
        