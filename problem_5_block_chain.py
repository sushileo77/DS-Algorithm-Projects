import hashlib

class Block: #Block Class
    def calc_hash(self): # Calculate the Hash Value
        sha = hashlib.sha256()
        hash_str = "We are going to encode this string of data!".encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __init__(self, timestamp, data, previous_hash): #Init Method
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.head=None
        
    
class Blockchain:
    def __init__(self):
        self.head = None
        self.tail = None

    def dict_rep(self): # Represent as a Dict {hash}
        block={}
        block['timestamp'] = self.timestamp
        block['data'] = self.data
        block['previous_hash'] = self.previous_hash
        block['hash'] = self.calc_hash()
        print(block['timestamp'])
  
        
    def __str__(self):
        return ''.join(str(o) for o in self)
        return self.__timestamp__
        return self.__data__
        return self.__hash__
        return self.hash

    def add_block(self,timestamp,data,previous_hash): # Add Block to the Block Chain
        if self.head is None:
            self.head=Block(timestamp=timestamp,data=data,previous_hash=0)
            self.tail=self.head
            return
        
        new_block = Block(timestamp=timestamp,data=data,previous_hash=previous_hash)
        new_block.previous_hash = self.hash # Link by Hashing
    
      

    def size(self): # Return Size
        """ Return the size or length of the linked list. """
        size = 0
        new_block = self.head
        while new_block:
            size += 1
            #node = Block.previous_hash

        return size
        
    
b=Blockchain()
b.add_block(100,500,2)
b.dict_rep

b1=Blockchain()
b1.add_block(110,200,4)
b1.dict_rep

#Corner Case [Empty Block Chain]
b2=Blockchain()
b2.add_block(0,0,0)
b2.dict_rep

#Corner Case [Current Cash, Same as Previous Hash]
b3=Blockchain()
b_hash=Block

b3.add_block(0,0,b_hash.calc_hash)
b3.dict_rep
