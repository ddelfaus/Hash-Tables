# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
       
        #get the index  from hash
        index = self._hash_mod(key)
        
        # check if the spot is available and add it
        if self.storage[index] is not None:
            print("something is there")
            #need a new node
            newNode = LinkedPair(key, value)
            #need to point to the next node
            newNode.next = self.storage[index]
            #store it
            self.storage[index] = newNode
            # print("value of node", newNode.value )
        else:
            self.storage[index] = LinkedPair(key,value)


        #    # #increase size
        # # self.size += 1
        # #get the index  from hash
        # index = self._hash_mod(key)
        # # print(index)
        # # select = self.storage[index]
        # # print(select)
        # # check if the spot is available and add it
        # if self.storage[index] is not None:
        #     #collision
        #     print("something is there")
        #     #need to create a new node
        #     # newNode = LinkedPair(key, value)
        #     # #point to the next node
        #     # # newNode.next = self.storage[index]
        #     # print(newNode)
        #     # self.storage[index] = newNode
        #     return
    
        # self.storage[index] = LinkedPair(key,value)


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        #need to get index from hash
        index = self._hash_mod(key)
        # check if something is there
        if self.storage[index] is None:
            print("not found")
        #if there is something get rid of it
        else:
            self.storage[index] = None
    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        
        index = self._hash_mod(key)
        current_key = self.storage[index]
     
        while current_key:
            if current_key.key != key:
                current_key = current_key.next
            else:
            
                return current_key.value

        return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        #need to store old stuff

        # old_stuff = self.storage
        # #double new storage
        # self.capacity = self.capacity * 2
        # self.storage = self.capacity * [None]

        # for item in old_stuff:
        #     print(item)
        #     current_item = item
        #     while current_item is not None:

        #         self.insert(current_item.key, current_item.value)
        #         current_item = current_item.next
        self.capacity *= 2
        old_stuff = self.storage
        self.storage = self.capacity * [None]

        for pervious_keys in old_stuff:
            current_key = pervious_keys
            while current_key is not None:
                self.insert(current_key.key, current_key.value)
                current_key = current_key.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    print("2",ht.retrieve("line_2"))
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print("1",ht.retrieve("line_1"))
    print("2",ht.retrieve("line_2"))
    print("3", ht.retrieve("line_3"))
    print(ht.remove("line_3"))
    print("3", ht.retrieve("line_3"))
    print("2", ht.retrieve("line_2"))
    print("1",ht.retrieve("line_1"))
    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
