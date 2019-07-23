class Node(object): # Create a Node Class Object 
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        
class LRU_Cache(object): # Create a LRU Cache Object
    def __init__(self, capacity):
        # Initialize class variables
        self.hash_map = {} # Declare a Dict {Hash Map to store values in cache as key,value pair}
        self.head = None
        self.end = None
        self.capacity = capacity
        self.current_size = 0


    def set_head(self, node):
        if not self.head:
            self.head = node #only one node
            self.end = node
        else:
            node.prev = self.head #insert a node after head
            self.head.next = node
            self.head = node
        self.current_size += 1


    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key == '':
            print("Null pointer! Please Try to specify a Valid Index")
        if key not in self.hash_map: # Takes care even if we sent key as 0
            return -1
        
        node = self.hash_map[key]
        if self.head == node:
            return node.value
        self.remove(node)
        self.set_head(node)
        return node.value
        
    def set(self, key, value):
        # Set the value if the key is not present in the cache. 
        if key in self.hash_map: # If key is present, assign to the Hash Map
            node = self.hash_map[key]
            node.value = value

            if self.head != node:
                self.remove(node)
                self.set_head(node)
        else:
            new_node = Node(key, value)
            if self.current_size == self.capacity:
                del self.hash_map[self.end.key]
                self.remove(self.end)
            self.set_head(new_node) # Assign a new value as a Head of Linked List
            self.hash_map[key] = new_node
            
    def remove(self, node): # Remove from Rear end of the Linked List
        if not self.head:
            return

        # removing the node form between the list
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        # head = end = node
        if not node.next and not node.prev:
            self.head = None
            self.end = None

        # if the node we are removing is the one at the end, update the new end
        # also not completely necessary but set the new end's previous to be NULL
        if self.end == node:
            self.end = node.next
            self.end.prev = None
        self.current_size -= 1
        return node

our_cache = LRU_Cache(2)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3,3)
#Corner Case (Trying to Get Element removed from Cache)
our_cache.get(1)       # Output :- returns -1
our_cache.get(2)       # Output :-returns 2
our_cache.get(3)       # Output :-return 3
#Give Zero Element Key to be fetched {Corner Case}
our_cache.get(0)       # Output :- return -1
#Give Very Large Element Key to be fetched {Corner Case}
our_cache.get(1024) #Output :- -1
