class Node:
    def __init__(self, data):
        self.data = data

class LRUCache:
      
    def __init__(self, cap):
        
        self._map = {}
        self.revmap = {}
        self._list = []
        self.size = cap
        
    def get(self, key):
        
        item = self._map.get(key, None)
        if item:
            value = item.data
            
            self._list.remove(item)
            node = Node(value)
            self._list.append(node)
            
            self._map[key] = node
            self.revmap[node] = key
            return value
        return -1 
            
    def put(self, key, value):
        node = self._map.get(key, None)
        if node:
            node.data = value
            self._list.remove(node)
            self._list.append(node)
            return
        elif len(self._list) == self.size:
            item = self._list[0]
            self._list.pop(0)
            _key = self.revmap[item]
            del self._map[_key]
            del self.revmap[item]
        node = Node(value)
        self._list.append(node)
        self._map[key] = node
        self.revmap[node] = ke