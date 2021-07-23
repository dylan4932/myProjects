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

# DocString Test
doctest.testmod()

