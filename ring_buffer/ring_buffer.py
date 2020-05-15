from doubly_linked_list import DoublyLinkedList



class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        
    def append(self, item):
    #check if ring buffer is full 
        if self.storage.length < self.capacity:
        #if not full add item / set current to head 
            self.storage.add_to_tail(item)
            self.current = self.storage.head
            return #keep doing till it is at capacity
        #when it is at capacity
        else:
            self.current.value = item 
            #make current the item 
            #if current is the tail then set it to the head
            if self.current == self.storage.tail:            
                self.current = self.storage.head
            
            else:
                self.current = self.current.next
            #step current to next node
                   
    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        node = self.storage.head
        #start at head add it and step to next and add node to the list
        while node:
            list_buffer_contents.append(node.value)
            node = node.next
       
               
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity        
        
        
        

    def append(self, item):
        pass

            

    def get(self):
        pass
