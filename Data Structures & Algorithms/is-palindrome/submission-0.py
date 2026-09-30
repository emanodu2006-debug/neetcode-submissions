class Solution:
    def isPalindrome(self, s: str) -> bool:
        reversed_string = ""
        
        if len(s) < 1:
            return False
        
        combined_string = s.replace(" ", "")
        combined_string = combined_string.lower()
        combined_string = "".join(c for c in combined_string if c.isalnum())

        for i in range(len(combined_string) - 1, -1, -1):
            reversed_string += combined_string[i]

        if reversed_string == combined_string:
            return True

        return False
