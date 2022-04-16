# Runtime: 55 ms, faster than 37.85% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 15.4 MB, less than 98.38% of Python3 online submissions for Reverse Linked List.
class Solution:
    def reverseList(self, head):
        if head == None:
            return head
        else:
            prevNode, currNode = head, head
            while currNode != None:
                if prevNode == currNode:
                    currNode = currNode.next
                    prevNode.next = None
                else:
                    nextNode = currNode.next
                    currNode.next = prevNode
                    prevNode = currNode
                    currNode = nextNode
        return prevNode