class Solution:

    def encode(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            strs[i] = strs[i] + '¬'
        
        encoded_string = "".join(strs)
        
        return encoded_string



    def decode(self, s: str) -> List[str]:
        decoded_strs = s.split('¬')[:-1]


        return decoded_strs
