# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return 

        reordered = []
        curr = head
        while curr:
            reordered.append(curr)
            curr = curr.next

        i, j = 0, len(reordered) - 1

        while i < j:
            reordered[i].next = reordered[j]
            i += 1
            if i>= j:
                break

            reordered[j].next = reordered[i]
            j -= 1
        reordered[i].next = None
            

