class Solution:
    def reverseVowels(self, s: str) -> str:
        # 1. Collect all the vowels present in the string
        vowels = []
        for char in s:
            if char in "aeiouAEIOU":
                vowels.append(char)
        
        # 2. Reverse the list of vowels using simple slicing
        reversed_vowels = vowels[::-1]
        
        # 3. Rebuild the final answer string
        result = ""
        vowel_ptr = 0 # Keeps track of which reversed vowel to use next
        
        for char in s:
            if char in "aeiouAEIOU":
                # If it's a vowel, grab the one from our reversed list
                result += reversed_vowels[vowel_ptr]
                vowel_ptr += 1
            else:
                # If it's a consonant, keep it exactly as it was
                result += char
                
        return result
    

        