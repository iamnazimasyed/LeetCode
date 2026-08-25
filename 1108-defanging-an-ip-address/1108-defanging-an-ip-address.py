class Solution:
    def defangIPaddr(self, address: str) -> str:
        an = ""
        for i in range(len(address)):
            if address[i] == ".":
                an = an + "[.]"
            else:
                an = an + address[i]
        return an
        
         
        