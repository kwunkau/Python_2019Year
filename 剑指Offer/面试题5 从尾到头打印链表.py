# -*- coding: utf-8 -*-

'''
【题目】：
输入一个链表的头节点，从尾到头打印每个节点的值。

【解题思路】：
1. 栈： 每读出一个结点的值，压入栈中，最后出栈得到结果；
2. 递归： 每次先答应下一个节点的值再打印自身节点。
'''


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution:
#     # 返回从尾部到头部的列表值序列，例如[1,2,3]
#     def printListFromTailToHead(self, listNode):
#         # write code here
#         alist = []
#         head = listNode
#         while head:
#             alist.append(head.val)
#             head = head.next
#         return alist[::-1]
#
#
# line = "abcde"
# print(line[:-1])
# line1 = "abcde"
# print(line1[::-1])
