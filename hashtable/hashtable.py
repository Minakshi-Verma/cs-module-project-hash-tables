class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

#linkedlist class
class LinkedList:
    def __init__(self):
        self.head = None

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity, count=0):
        # Your code here
        if capacity > MIN_CAPACITY:
            self.capacity = capacity
            self.data = [LinkedList()] *capacity   #datastructure is now linkedlist
            self.count= count   # to keep tack of number of elements(setDefault=0)  
        else:
            self.capacity = MIN_CAPACITY
            self.data = [LinkedList()] * capacity
            self.count= count


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.data)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.count/len(self.data)

#----------------fnv1 hash function ------------
    def fnv1(self, key, seed=0):
    # def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        """
        Returns: The FNV-1 hash (64-bit) of a given string. 
        """
        #Constants : Fails the tests
        # FNV_prime = 1099511628211
        # offset_basis = 14695981039346656037

        # #FNV-1a Hash Function
        # hash = offset_basis + seed
        # # hash = offset_basis
        # for c in key:
        #     hash = hash * FNV_prime
        #     hash = hash ^ ord(c)
        # return hash

        """
        Returns: The FNV-1a (alternate) hash of a given string
        """
        # #Constants : Passes the tests
        # FNV_prime = 1099511628211
        # offset_basis = 14695981039346656037

        # #FNV-1a alternate Hash Function
        # hash = offset_basis + seed
        # for c in key:
        #     hash = hash ^ ord(c)
        #     hash = hash * FNV_prime
        # return hash

#----------------djb2 hash function------------
    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for c in key:
            hash = (hash*33)+ ord(c)
        return hash    


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity


    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        # check for linkedlist if it is empty
        if self.data[index].head == None:
            self.data[index].head = HashTableEntry(key, value)  # similar to node class we used before
            self.count +=1
            # #-----
            # self.loadfactor = self.count / self.capacity
            # if self.loadfactor > 0.7:
            #     self.resize(self.capacity * 2)
            
        else:
            # Linklist is not empty 
            # create reference for the head node
            cur= self.data[index].head

            while cur.next:
                # checking if the key already exist then we will just override the value
                if cur.key == key:
                    cur.value == value
                # checking each node of the Linkedlist till we break the while loop    
                cur= cur.next
        # if key is not found, add the new hashtableentry(key, value) to the linkedlist
            cur.next = HashTableEntry(key, value)
            self.count +=1

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)        
        print(index)
        cur = self.data[index].head

        if cur.key==key:
            
            self.data[index].head = self.data[index].head.next
            # cur.next = self.data[index].head
            self.count -=1
            print("Warning:headnode deleted")          
        else:
            
            while cur.next:                
                prev = cur
                cur =cur.next
                if cur.key == key:
                    #to remove the current node, change the pointers
                    prev.next=cur.next                    
                    self.count -=1                    
              

            # return None
                

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here      
        index = self.hash_index(key)  
        cur = self.data[index].head    

        if cur==None:
            print("linked list is empty")
        elif cur.key== key:
            return cur.value
        else:
            while cur.next:
                cur= cur.next
                if cur.key ==key:                   
                    return cur.value 


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here     
        self.capacity= new_capacity
        new_data= [LinkedList()]* new_capacity        
        
        # resizing  of storage needed if loadfactor >0.7 or <0.2
        if self.get_load_factor() > 0.7:                
            #iterate through all the items in the orginal data
            for i in self.data:
                cur = i.head
                while cur:                                       
                    # rehash the key/value pairs of data with new_capacity and get the new index
                    
                    index = self.hash_index(cur.key)

                    # now add all the items to the new list
                    if new_data[index].head is None:
                        #make new node the head
                        new_data[index].head= HashTableEntry(cur.key, cur.value)
                    else:
                        new_node = HashTableEntry(cur.key, cur.value)
                        print("Keys",cur.key) 
                        print("Values",cur.value)
                        # add new_node to the head and shift the head pointers 
                        new_node.next = new_data[index].head
                        new_data[index].head = new_node
                    # repeat till all the nodes have been added to new storage    
                    cur = cur.next   
            # Once all the nodes have been added to new_data: self.data== new_data
        self.data= new_data

    

if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")








