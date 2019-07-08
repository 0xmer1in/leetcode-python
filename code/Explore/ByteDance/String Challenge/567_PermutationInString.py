class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        A = [ord(x) - ord('a') for x in s1]
        B = [ord(x) - ord('a') for x in s2]

        target = [0] * 26
        for x in A:
            target[x] += 1

        window = [0] * 26
        for i, x in enumerate(B):
            window[x] += 1
            if i >= len(A):
                window[B[i - len(A)]] -= 1
            if window == target:
                return True
        return False


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        L1, L2 = len(s1), len(s2)
        if L1 > L2:
            return False
        target, times = {chr(i): 0 for i in range(97, 123)}, {chr(i): 0 for i in range(97, 123)}
        for i in s1:
            target[i] += 1
        for i in s2[:L1]:
            times[i] += 1
        for i in range(1, L2 - L1 + 1):
            if times == target:
                return True
            times[s2[L1 - 1 + i]] += 1
            times[s2[i - 1]] -= 1
        return times == target