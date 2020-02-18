class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.order = DoublyLinkedList()
        self.storage = dict() #{}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage:
            node = self.storage[key]
            # MRU at the head(most recently used)
            self.order.move_to_front(node)
            return node
        else:
            return None
        

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # item already in cache
            if key in self.storage.keys():
            # get node from self.storage
            
            # move_to_front(), it's now MRU (at head)
            else: # new item needs to be cached
        # still have room in cache
            if self.size < self.limit:
                self.order.add_to_head(value)
                # add to dict
                self.storage[key] = self.order.head
                # add to head (MRU)
                # update size
                self.size += 1
            # add to head (MRU)
            else: # cache is full

# remove LRU(least recently used) from tail
# add to head (MRU)