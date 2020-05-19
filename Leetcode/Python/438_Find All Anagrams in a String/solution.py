class Solution:
    def findAnagrams(self, s: str, p: str) -> [int]:     
        # 26 Prime Values Declaration
        primes = [
            2, 3, 5, 7, 11, 13, 
            17, 19, 23, 29, 31, 
            37, 41, 43, 47, 53, 
            59, 61, 67, 71, 73, 
            79, 83, 89, 97, 101
        ]

        # Get Length of Args
        s_len, p_len = len(s), len(p)

        # Initialise Values
        hash_p = hash_temp = 1
        indexes = []

        for l in p:
            hash_p *= primes[ord(l) - 97]
        for l in s[:p_len]:
            hash_temp *= primes[ord(l) - 97]
        
        # Sliding Windows Method
        for i in range(s_len - p_len):
            if hash_p == hash_temp:
                indexes.append(i)
            if s[i] != s[i + p_len]:
                hash_temp //= primes[ord((s[i])) - 97]
                hash_temp *= primes[ord((s[i + p_len])) - 97]

        # Check Final Iteration
        if hash_p == hash_temp:
            indexes.append(s_len - p_len)
                
        # Return Indexes that is an Anagram
        return indexes
