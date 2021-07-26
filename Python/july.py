##############June practice##############
#########################################
import doctest

############July 6th#####################

def twoSum0(nums, target):
    '''Given an array of integers nums and an integer target, return indices
       of the two numbers such that they add up to target.

       You may assume that each input would have exactly one solution, and
       you may not use the same element twice.

       You can return the answer in any order.

       >>> nums = [2, 7, 11, 15]
       >>> target = 9
       >>> twoSum0(nums, target)
       [0, 1]

       >>> nums = [3, 2, 4]
       >>> target = 6
       >>> twoSum0(nums, target)
       [1, 2]

       >>> nums = [3, 3]
       >>> target = 6
       >>> twoSum0(nums, target)
       [0, 1]
    '''
    for index in range(len(nums)):
        cur = index + 1
        for nxt in range(cur, len(nums)):
            if nums[index] + nums[nxt] == target:
                return list([index, nxt])           # runtime: n^2

def twoSum1(nums, target):
    '''Given an array of integers nums and an integer target, return indices
       of the two numbers such that they add up to target.

       You may assume that each input would have exactly one solution, and
       you may not use the same element twice.

       You can return the answer in any order.

       >>> nums = [2, 7, 11, 15]
       >>> target = 9
       >>> twoSum1(nums, target)
       [0, 1]

       >>> nums = [3, 2, 4]
       >>> target = 6
       >>> twoSum1(nums, target)
       [1, 2]

       >>> nums = [3, 3]
       >>> target = 6
       >>> twoSum1(nums, target)
       [0, 1]
    '''
    nums_sorted = sorted(nums)

    l = 0
    r = len(nums) - 1

    if len(nums) == 2:
        return list([0, 1])
    else:
        while l != r:
            if nums_sorted[l] + nums_sorted[r] < target:
                l += 1
            elif nums_sorted[l] + nums_sorted[r] > target:
                r -= 1
            else:
                if nums.index(nums_sorted[l]) == nums.index(nums_sorted[r]):
				    # to deal with scenario that list has repeated elements, e.g., [3,1,3]
                    return list([nums.index(nums_sorted[l]), nums.index(nums_sorted[r], nums.index(nums_sorted[l])+1)])
                else:				    # to deal with scenario where list has no repeated elements, e.g., [1,2,3]
                    return list([nums.index(nums_sorted[l]), nums.index(nums_sorted[r])])

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def addTwoNumbers(l1, l2):
    '''
    You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order, and each of their nodes contains a single digit.
    Add the two numbers and return the sum as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    
    >>> l = ListNode(2, ListNode(4, ListNode(3, None)))
    >>> g = ListNode(5, ListNode(6, ListNode(4, None)))
    >>> res = addTwoNumbers(l, g)
    >>> res.val
    7
    >>> res.next.val
    0
    >>> res.next.next.val
    8

    >>> l = ListNode(0)
    >>> g = ListNode(0)
    >>> res = addTwoNumbers(l, g)
    >>> res.val
    0

    >>> l = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    >>> g = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    >>> res = addTwoNumbers(l, g)
    >>> res.val
    8
    >>> res.next.val
    9
    >>> res.next.next.val
    9
    >>> res.next.next.next.val
    9
    >>> res.next.next.next.next.val
    0
    >>> res.next.next.next.next.next.val
    0
    >>> res.next.next.next.next.next.next.val
    0
    >>> res.next.next.next.next.next.next.next.val
    1
    '''
    sum = format(l1) + format(l2)
    sum_str = str(sum)
    l = len(sum_str) - 1
    res = ListNode(int(sum_str[l]))
    cur = res
    while l >= 0:
        l -= 1
        cur.next = ListNode(int(sum_str[l]))
        cur = cur.next
    return res
    
def format(l1):
    s = ''
    while l1:
        s += str(l1.val)
        l1 = l1.next
    s = s[::-1]
    return int(s)


##################July 23th########################
def lengthOfLongestSubstring(s):
    '''
    LEETCODE #3
    Given a string s, find the length of the longest substring without
    repeating characters.

    >>> lengthOfLongestSubstring('bbbbb')
    1
    >>> lengthOfLongestSubstring('abcabcbb')
    3
    >>> lengthOfLongestSubstring('pwwkew')
    3
    >>> lengthOfLongestSubstring('')
    0
    '''
    charSet = set()
    l = 0
    res = 0
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r-l+1)
    return res

def longestPalindrome(s):
    '''
    Given a string s, return the longest palindromic substring in s

    >>> longestPalindrome('babad')
    'bab'
    >>> longestPalindrome('ccc')
    'ccc'
    >>> longestPalindrome('cbbd')
    'bb'
    >>> longestPalindrome('a')
    'a'
    >>> longestPalindrome('ac')
    'a'
    
    '''
    res = ""
    resLen = 0
        
    for i in range(len(s)):
            # odd length panlidrome
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                res = s[l:r+1]
                resLen = r - l + 1
            l -= 1
            r += 1
               
            # even length panlidrome
        l, r = i, i+1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r-l + 1) > resLen:
                res = s[l:r+1]
                resLen = r - l + 1
            l -= 1
            r += 1
    return res

##############July 26th
def romanToInt(s):
    '''
    Roman numerals are represented by seven different symbols:
    I, V, X, L, C, D and M.

    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    For example, 2 is written as II in Roman numeral,
    just two one's added together. 12 is written as XII,
    which is simply X + II. The number 27 is written as XXVII,
    which is XX + V + II.

    Roman numerals are usually written largest to smallest from
    left to right. However, the numeral for four is not IIII.
    Instead, the number four is written as IV. Because the one
    is before the five we subtract it making four. The same principle
    applies to the number nine, which is written as IX. There are six
    instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.
    Given a roman numeral, convert it to an integer.
    
    >>> romanToInt('III')
    3
    >>> romanToInt('IV')
    4
    >>> romanToInt('IX')
    9
    >>> romanToInt('LVIII')
    58
    >>> romanToInt('MCMXCIV')
    1994
    '''
    dict0 = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    list0 = []
    list0[:0] = s
    list0.append('I')
    ans = 0
    for i in range(len(list0)-1):
        if dict0[list0[i]] >= dict0[list0[i+1]]:
            ans += dict0[list0[i]]
        else:
            ans -= dict0[list0[i]]
    return ans

def longestCommonPrefix(strs):
    '''
    Write a function to find the longest common prefix string amongst
    an array of strings.

    If there is no common prefix, return an empty string "".

    >>> longestCommonPrefix(['flow', 'flower', 'flight'])
    'fl'
    >>> longestCommonPrefix(["dog","racecar","car"])
    ''
    >>> longestCommonPrefix(['sunshine', 'sunflower', 'sunroof'])
    'sun'
    '''
    res = ''
    cur = sorted(strs)
    for i in cur[0]:
        if cur[-1].startswith(res+i):
            res += i
        else:
            break
    return res

# DocString Test
doctest.testmod()

