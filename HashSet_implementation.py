
class MyHashSet:
    def __init__(self):
        self.bucket_count = 1000
        self.buckets = [[] for _ in range(self.bucket_count)]


    def _simple_hash(self, key):
        if isinstance(key, int):
            # for integers , just return the element modulo bucket_count
            return key % self.bucket_count
        
        elif isinstance(self, str):
            # for str sum the ASCII values of str
            hash_value = sum(ord(char) for char in key)
            return hash_value % self.bucket_count
        
        else:
            # raise error for unsupported types
            raise TypeError("Unsupported type of hashing")
        
    def add(self, key):
        index = self._simple_hash(key) # compute the index using function
        if key not in self.buckets[index]:
            self.buckets[index].append(key)
            

    def contain(self, key):             
        index = self._simple_hash(key)  # compute the index using function
        return key in self.buckets[index]
    
    def remove(self, key):             
        index = self._simple_hash(key)   # compute the index using function
        if key in self.buckets[index]:
            self.buckets[index].remove(key)


# Create a hash set
my_set = MyHashSet()

# Add elements to the hash set
my_set.add(10)
my_set.add(20)
my_set.add(30)

# Check if elements are in the hash set
print(my_set.contain(10))  # Output: True
print(my_set.contain(25))  # Output: False

# Remove an element from the hash set
my_set.remove(20)

# Check again
print(my_set.contain(20))  # Output: False