class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = str(x)
        reverse_word= original[::-1]    # reverse orider using slicing
        #check
        # print(original) 
        # print(reverse_word)
        if original == reverse_word:
          return True 