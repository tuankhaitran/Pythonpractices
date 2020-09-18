# Using array and list to implement own Hash Table
import numpy
class HashTable:
    def __init__(self, size):
        self.data = numpy.empty(size, dtype=object)
        self.size=size

    # Hash Function
    def _hash(self,key):
        hash=0
        for i in range(len(key)):
            hash= (hash + ord(key[i]) * i) % self.size
        return hash
        
    def set(self, key,value):
        address=self._hash(key)

        # In case where the address not been occupied
        if (self.data[address]==None):
            self.data[address]=[]
            self.data[address].append([key,value])
        # In case where the address has been occupied
        else:
            self.data[address].append([key,value])

    def get(self, key):
        # Calculate the address
        address=self._hash(key)
        currentBucket = self.data[address]

        # If the key is valid
        if currentBucket:
        # Loop through and search for the correct key
            for eachpair in currentBucket:
                if eachpair[0] == key:
                    return eachpair[1]
        # If key is invalid just return None
        else:
            return None      

    def keys(self):
        keysArray=[]
        # Loop through the array
        for item in self.data:
        # Check if the address has a value
            if item:
                for i in item:
                    keysArray.append(i[0])
        return keysArray

myHashTable = HashTable(2)
myHashTable.set('grapes', 10000)
myHashTable.set('orange', 5000)
myHashTable.set('apple', 60000)
myHashTable.set('pear', 4300)

print(myHashTable.keys())

