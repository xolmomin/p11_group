class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f'{self.val}->{self.next}'


class LinkedList:
    def __init__(self, val=0, next=None):
        self.head = ListNode(val, next)

    def from_list(self, a: list) -> None:
        tmp = self.head
        for i in a:
            tmp.next = ListNode(i)
            tmp = tmp.next

        self.head = self.head.next

    def print_ll(self) -> None:
        tmp = self.head
        while tmp:
            print(tmp.val, end=' ')
            tmp = tmp.next

    def length(self) -> int:
        tmp = self.head
        count = 0
        while tmp:
            count += 1
            tmp = tmp.next
        return count

    def example(self) -> int:
        tmp = self.head
        s = 0
        while tmp:
            s = s * 2 + tmp.val
            tmp = tmp.next
        return s




# a = [1,2,3,4,5]
#
# ll = LinkedList()
# ll.from_list(a)
# print(ll.example())
list1 = [1,2,4]
list2 = [1,3,4]


# Output: [1,1,2,3,4,4]
# print(ll.head)
# ll.print_ll()


# node_5 = ListNode(5)
# node_4 = ListNode(4, node_5)
# node_3 = ListNode(3, node_4)
# node_2 = ListNode(2, node_3)
# node_1 = ListNode(1, node_2)
#
#
# tmp = node_1
# while tmp:
#     if tmp.val & 1:
#         print(tmp.val, end=' ')
#     tmp = tmp.next
# tmp = node_1
# print()
#
# while tmp:
#     if not tmp.val & 1:
#         print(tmp.val, end=' ')
#     tmp = tmp.next
#
# print()
# print(node_1)
# # head = node_1
# #
# # tmp = head
# #
# # # from itertools import cycle
# # #
# # # for i in cycle([1]):
# # #     if not tmp:
# # #         break
# # #     print(tmp.val, end=' ')
# # #     tmp = tmp.next
# #
# # while tmp:
# #     print(tmp.val, end=' ')
# #     tmp = tmp.next
# #
# # print()
# # print(head)
#
#
# # row3.next = node_2
# # node_2.next = node_3
# # node_3.next = node_4
# # node_4.next = node_5
# #
# # row4 = ListNode(8)
# # node_7 = ListNode(9)
# # node_8 = ListNode(4)
# # row4.next = node_7
# # node_7.next = node_8
# # node_8.next = node_4
# #
# # row5 = ListNode(3)
# # node_9 = ListNode(6)
# # row5.next = node_9
# # node_9.next = node_7
# #
# # row6 = ListNode(8)
# # node_10 = ListNode(9)
# # node_11 = ListNode(7)
# #
# # row6.next = node_10
# # node_10.next = node_11
# # node_11.next = node_8
# #
# # row1 = ListNode(2)
# # row1.next = node_2
# #
# #
# # row2 = ListNode(3)
# # row2.next = node_3
# #
# #
# # print(row1)
# # print(row2)
# # print(row3)
# # print(row4)
# # print(row5)
# # print(row6)
# #
# #
