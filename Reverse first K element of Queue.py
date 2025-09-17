class Node:
  class Solution:
    def reverseFirstK(self, q, k):
         
        size = len(q)
        
        
        if size < k:
            return list(q)
        
        store_post_k = []
        st = []

        
        for _ in range(k, size):
            store_post_k.append(q.pop())

        
        for _ in range(k):
            st.append(q.pop())
        
        
        size = len(store_post_k)
        for i in range(size - 1, -1 , -1):
            st.append(store_post_k[i])

        return st