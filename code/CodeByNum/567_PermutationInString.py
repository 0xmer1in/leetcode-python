class Solution:
    def dsa(self, s1: str, s2: str) -> bool:
        A = [ord(i) - ord('a') for i in s1]
        B = [ord(i) - ord('a') for i in s2]

        target = [0] * 26
        for i in A:
            target[i] += 1

        window = [0] * 26
        for i, item in enumerate(B):
            window[item] += 1
            if i >= len(A):
                window[B[i - len(A)]] -= 1
            if window == target:
                return True
        return False