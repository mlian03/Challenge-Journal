class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def generate(arr):
        node = startNode = ListNode(arr[0])
        for v in arr[1:]:
            node.next = ListNode(v)
            node = node.next
        return startNode
