class Solution:
    def romanToInt(self, s: str) -> int:
        roman_int_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        s_elem = list(s)
        # print(s_elem)     # str to list
        
        s_int = [roman_int_dict[i] for i in s_elem]
        # print(s_int)      # change to int
        
        sum = 0
        for i in range(len(s_int)):
            if i != len(s_int)-1:
                if (s_int[i] == 1 and s_int[i+1] in [5, 10]) or (s_int[i] == 10 and s_int[i+1] in [50, 100]
                ) or (s_int[i] == 100 and s_int[i+1] in [500, 1000]):
                    sum = sum-s_int[i]
                else:
                    sum = sum + s_int[i]
            else:
                sum = sum + s_int[i]
        return sum