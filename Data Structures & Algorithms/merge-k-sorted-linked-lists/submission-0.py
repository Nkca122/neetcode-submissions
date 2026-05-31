class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Dummy node simplifies head management
        dummy = ListNode(0)
        tail = dummy
        heap = []
        
        # Put the head of each non-empty list into the heap
        # We include `id(node)` as a tie-breaker because Python's heapq 
        # compares tuples element by element, and ListNode doesn't have a '<' operator.
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
                
        while heap:
            val, i, node = heapq.heappop(heap)
            
            # Append the node to our result list
            tail.next = node
            tail = tail.next  # Move the tail pointer forward O(1)
            
            # If this list has more nodes, push the next one into the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
                
        return dummy.next