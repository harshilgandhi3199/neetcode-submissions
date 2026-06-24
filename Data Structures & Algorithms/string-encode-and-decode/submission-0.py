class Solution:

    def encode(self, strs: List[str]) -> str:
        # "hello", "world" -> "5/hello5/world"
        # keep length and string together
        encoded_str = ""
        for s in strs:
            count = len(s)
            encoded_str += f"{count}/"
            encoded_str += s

        print(encoded_str)
        return encoded_str
    
    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        "5/hello5/world"
        i = 0
        count = ""
        while i < len(s):
            if s[i] is not '/':
                count += s[i]
                i += 1
                continue
            count = int(count)
            curr_str = s[i+1: i+1+count] 
            decoded_strs.append(curr_str)
            i = i + 1 + count
            count = ""
            
        return decoded_strs
