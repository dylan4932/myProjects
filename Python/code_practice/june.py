import unittest
def equalFrequency(word):
        """
        :type word: str
        :rtype: bool
        """
        counts = dict()
        for i in word:
            counts[i] = counts.get(i, 0) + 1
        return set(counts.values())


def lengthOfLIS(nums, k):
    """

    >>> lengthOfLIS([4, 2, 1, 4, 3, 4, 5, 8, 15], 3)
    5
    >>> lengthOfLIS([7, 4, 5, 1, 8, 12, 4, 7], 5)
    4
    >>> lengthOfLIS([1, 5], 1)
    1
    """
    re = []
    for i in range(len(nums)):
        j, l = i, [nums[i]]
        while j < len(nums) - 1:
            if nums[j+1] - nums[j] < k:
                l.append(nums[j+1])
            j+=1
        re.append(len(l))
    return max(re)

def repeatedSubstringPattern(s) -> bool:
        #n = len(s)
        #for i in range(1, n // 2 + 1):
        #    if n % i == 0:
        #        if all(s[j] == s[j - i] for j in range(i, n)):
        #            return True
        #return False
    n = 1
    while n < len(s)//2+1:
        if len(s)%n == 0:
            if all([s[:n] == s[j:j+n] for j in range(n, len(s), n)]):
                return True
        n+=1
    return False

def repeatSubstring(s) -> bool:
    return (s + s).find(s, 1) != len(s)

def lengthOfLongestSubstring( s):
    """
    """
    occ = set()
    n = len(s)
    rk, ans = -1, 0

    for i in range(n):
        if i != 0:
            occ.remove(s[i - 1])
        while rk + 1 < n and s[rk + 1] not in occ:
            occ.add(s[rk + 1])
            rk += 1
        ans = max(ans, rk - i + 1)
    return ans

def int2Bit(x, y):
    xbit = f'{x:08b}'
    ybit = f'{y:08b}'
    return xbit, ybit


s = "()[]{}"
[idx for idx in range(len(s))]

if __name__=='__main__':
	unittest.main()
