import unittest
import re
# import numpy


def climb_stairs(n):
    """
    Fibonacci Sequence
    :type n: int
    :rtype: int
    >>> climb_stairs(3)
    3
    >>> climb_stairs(2)
    2
    """
    a = b = 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b


def my_atoi(s):
    """
    Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32).
    If no digits were read, then the integer is 0. Change the sign as necessary

    >>> my_atoi("123")
    123
    >>> my_atoi("0032")
    32
    >>> my_atoi("words and 987")
    987
    >>> my_atoi("     -42")
    -42
    >>> my_atoi(" +86-183")
    86
    """

    digits = re.findall(r'-?\d+', s)
    if not digits:
        return 0
    return int(digits[0])


def longest_common_prefix(strs):
    """
    >>> longest_common_prefix(["cir", "car"])
    'c'
    >>> longest_common_prefix(["flower","flow","flight"])
    'fl'
    >>> longest_common_prefix(["dog","racecar","car"])
    ''
    """
    if len(strs) == 1:
        return strs[0]

    prefix = set()
    curr = ""
    min_len = min([len(word) for word in strs])

    for i in range(min_len):
        if len(set([ch[i] for ch in strs])) == 1:
            curr += strs[0][i]
            prefix.add(curr)
        else:
            break

    if prefix:
        return max(prefix)
    else:
        return ""


def equal_frequency(word):
    """
    Given a 0-indexed string word, consisting of lowercase English letters.
    You need to select one index and remove the letter at that index from word
    so that the frequency of every letter present in word is equal.

    Return true if it is possible to remove one letter so that the frequency of
    all letters in word are equal, and false otherwise.

    Note:
    The frequency of a letter x is the number of times it occurs in the string.
    You must remove exactly one letter and cannot choose to do nothing.
    >>> equal_frequency("abcc")
    True
    >>> equal_frequency("aazz")
    False
    """
    # Approach #1
    counts = dict()
    choice = 1
    for ch in word:

        if ch in counts and choice > 0:
            counts[ch] -= 1
            choice -= 1

        counts[ch] = counts.get(ch, 0) + 1
    return len(set(counts.values())) == 1

    # Approach # 2
    # for i in range(len(word)):  # 枚举删除的字符
    #     cnt = Counter(word[:i] + word[i + 1:])  # 统计出现次数
    #     if len(set(cnt.values())) == 1:  # 出现次数都一样
    #         return True
    # return False


# def lengthOfLIS(nums, k):
#     """
#
#     >>> lengthOfLIS([4, 2, 1, 4, 3, 4, 5, 8, 15], 3)
#     5
#     >>> lengthOfLIS([7, 4, 5, 1, 8, 12, 4, 7], 5)
#     4
#     >>> lengthOfLIS([1, 5], 1)
#     1
#     """
#     re = []
#     for i in range(len(nums)):
#         j, l = i, [nums[i]]
#         while j < len(nums) - 1:
#             if nums[j+1] - nums[j] < k:
#                 l.append(nums[j+1])
#             j+=1
#         re.append(len(l))
#     return max(re)

def repeated_substring_pattern(s) -> bool:
    """

    """
    # n = len(s)
    # for i in range(1, n // 2 + 1):
    #    if n % i == 0:
    #        if all(s[j] == s[j - i] for j in range(i, n)):
    #            return True
    # return False
    n = 1
    while n < len(s) // 2 + 1:
        if len(s) % n == 0:
            if all([s[:n] == s[j:j + n] for j in range(n, len(s), n)]):
                return True
        n += 1
    return False


def repeat_substring(s) -> bool:
    """

    """
    return (s + s).find(s, 1) != len(s)


def int2bit(x, y):
    xbit = f'{x:08b}'
    ybit = f'{y:08b}'
    return xbit, ybit


def length_of_longest_substring(s):
    """
    Given a string s, find the length of the longest
    substring without repeating characters.

    >>> length_of_longest_substring("abcabcbb")# The answer is "abc", with the length of 3
    3
    >>> length_of_longest_substring("bbb") # The answer is "b",
    1
    >>> length_of_longest_substring("pwwkew") # "wke"
    3
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


def two_sum(nums, target):
    """
    Given an array of integers nums and an integer target,
    return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution,
    and you may not use the same element twice.
    You can return the answer in any order.

    >>> two_sum([2, 7, 11, 15], 9)
    [0, 1]
    >>> two_sum([3, 2, 4], 6)
    [1, 2]
    >>> two_sum([3, 3], 6)
    [0, 1]
    """
    hash_map = dict()
    for idx, num in enumerate(nums):
        if target - num in hash_map:
            return [hash_map[target - num], idx]
        hash_map[num] = idx
    return []


def three_sum(nums):
    """
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
    such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
    Notice that the solution set must not contain duplicate triplets.

    >>> three_sum([0, 1, 1])
    []
    >>> three_sum([0, 0, 0])
    [[0, 0, 0]]
    >>> three_sum([-1, 0, 1, 2, -1, -4])
    [[-1, -1, 2], [-1, 0, 1]]
    """

    n = len(nums)
    nums.sort()
    ans = list()

    for first in range(n):
        if first > 0 and nums[first] == nums[first - 1]:
            continue

        third = n - 1
        target = -nums[first]

        for second in range(first + 1, n):
            if second > first + 1 and nums[second] == nums[second - 1]:
                continue

            while second < third and nums[second] + nums[third] > target:
                third -= 1

            if second == third:
                break
            if nums[second] + nums[third] == target:
                ans.append([nums[first], nums[second], nums[third]])

    return ans


def is_valid(s):
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.

    An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    >>> is_valid("()")
    True
    >>> is_valid("()[]{}")
    True
    >>> is_valid("(]")
    False
    """

    if len(s) % 2 == 1:
        return False
    check = {')': '(', '}': '{', ']': '['}

    stack = list()
    for ch in s:
        if ch in check:
            if not stack or stack[-1] != check[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)
    return not stack


def max_subarray(nums):
    """
    Given an integer array nums, find the subarray with the largest sum, and return its sum.

    >>> max_subarray([-2,1,-3,4,-1,2,1,-5,4])
    6
    >>> max_subarray([1])
    1
    >>> max_subarray([5,4,-1,7,8])
    23
    >>> max_subarray([-2, -1])
    -1
    """
    max_sum = sum(nums)
    n = len(nums)
    if n == 1:
        return max_sum

    for i in range(n):
        if nums[i] > max_sum:
            max_sum = nums[i]

        for j in range(i + 1, n + 1):
            if sum(nums[i: j]) > max_sum:
                max_sum = sum(nums[i:j])
    return max_sum


def average_value(nums):
    """
    Given an integer array nums of positive integers, return the average value of all
    even integers that are divisible by 3.

    Note that the average of n elements is the sum of the n elements divided by n and
    rounded down to the nearest integer.
    >>> average_value([1,3,6,10,12,15])
    9
    >>> average_value([1,2,4,7,10])
    0
    >>> average_value([4,4,9,10])
    0
    >>>
    """
    evens = [num for num in nums if num % 2 == 0]
    res = [num for num in evens if num % 3 == 0]

    if not res:
        return 0
    else:
        return int(sum(res) / len(res))


def min_subarray_len(target, nums):
    """
    Given an array of positive integers nums and a positive integer target, return the minimal length of a
    subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

    >>> min_subarray_len(7, [2,3,1,2,4,3])
    2
    >>> min_subarray_len(4, [1, 4, 4])
    1
    >>> min_subarray_len(11, [1,1,1,1,1,1,1,1])
    0
    """
    res = []
    for idx, num in enumerate(nums):
        sum_arr = list()
        end = idx
        while end < len(nums):
            sum_arr.append(nums[end])
            if sum(sum_arr) >= target:
                res.append(len(sum_arr))
            end += 1
    if not res:
        return 0
    return min(res)



if __name__ == '__main__':
    unittest.main()