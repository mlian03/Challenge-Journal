class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 26 Prime Values Declaration
        primes = [
            2, 3, 5, 7, 11, 13, 
            17, 19, 23, 29, 31, 
            37, 41, 43, 47, 53, 
            59, 61, 67, 71, 73, 
            79, 83, 89, 97, 101
        ]

        # Get Length of Args
        s1_len, s2_len = len(s1), len(s2)

        # Initialise Values
        hash_s1 = hash_temp = 1

        for l in s1:
            hash_s1 *= primes[ord(l) - 97]
        for l in s2[:s1_len]:
            hash_temp *= primes[ord(l) - 97]
        
        # Sliding Windows Method
        for i in range(s2_len - s1_len):
            if hash_s1 == hash_temp:
                return True
            if s2[i] != s2[i + s1_len]:
                hash_temp //= primes[ord((s2[i])) - 97]
                hash_temp *= primes[ord((s2[i + s1_len])) - 97]

        # Check Final Iteration, return False if No Permutation
        return True if hash_s1 == hash_temp else False
