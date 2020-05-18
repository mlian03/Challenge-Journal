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
        lenS, lenP = len(s), len(p)

        # Initialise Values
        hashP = hashSub = 1
        indexes = []

        for l in p:
            hashP *= primes[ord(l) - 97]
        for l in s[:lenP]:
            hashSub *= primes[ord(l) - 97]
        
        # Sliding Windows Method
        for i in range(lenS - lenP):
            if hashP == hashSub:
                indexes.append(i)
            if s[i] != s[i + lenP]:
                hashSub //= primes[ord((s[i])) - 97]
                hashSub *= primes[ord((s[i + lenP])) - 97]

        # Check Final Iteration
        if hashP == hashSub:
            indexes.append(lenS - lenP)
                
        # Return Indexes that is an Anagram
        return indexes
