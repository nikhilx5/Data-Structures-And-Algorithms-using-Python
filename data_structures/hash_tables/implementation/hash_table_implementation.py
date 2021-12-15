"""
Hash Tables in Python are dictionary (key: value pairs)
All the keys are hashed and stored at random location in memory.
Due to limited memory space, there are chances of collisions. Collision happens when two keys have the conflict wrt to
same hash and are stored in same location in memory. In such cases, keys are linked to each other in the memory
(like linked list)

"""


class HashTable:

    def __init__(self, size):
        self.size = size
        self.basket = [[] for _ in range(self.size)]
        # self.data = [None] * self.size  # We initialize an array of size 'size' with None

    def __str__(self):
        return str(self.__dict__)

    # hash function to generate hash for a given key
    def _key_hash(self, key):
        hash_var = 0
        for i in range(len(key)):
            hash_var = (hash_var + ord(key[i]) * i) % self.size
        return hash_var

    def set(self, key, value):
        # generate hash for a given key
        address = self._key_hash(key)
        # add element to a given address in basket
        self.basket[address].append([key, value])

    def get(self, key):
        hashed_key = self._key_hash(key)
        # get the current bucket based on the hashed_key. This bucket can have one or many items
        current_bucket = self.basket[hashed_key]
        print(current_bucket)
        # approach 1 - using key in sub_bucket
        for sub_bucket in current_bucket:
            if key in sub_bucket:
                print(f"Key values are: {sub_bucket}")
        # approach 2 - using for loop and length of the current bucket
        # for i in range(len(current_bucket)):
        #     # for each element of the current bucket which itself is a list[], check if the first element (which is key)
        #     # matches the key supplied to the method. If it is match, send the associated value
        #     if current_bucket[i][0] == key:
        #         print(current_bucket[i][1])

    def keys(self):
        """
        Overall complexity: O(n^2)
        return all the keys of the hash tables
        :return:
        """
        keys = []
        for buckets in self.basket:  # O(n)
            if len(buckets) != 0:
                for sub_bucket in buckets:  # O(n)
                    keys.append(sub_bucket[0])

        print(keys)

    def values(self):
        """
        return all the values of the hash table
        :return:
        """
        values = []
        # loop through the entire basket
        for i in range(len(self.basket)):
            # check if the element exists at index basket[i]
            if self.basket[i]:
                # if element exists then loop through the length of that sub-basket
                for j in range(len(self.basket[i])):
                    # append all the values which are at sub-basket[1]
                    values.append(self.basket[i][j][1])

        print(values)

    def values_approach2(self):
        values_2 = []

        for bucket in self.basket:
            if len(bucket) != 0:
                # additional loop is required in case of collision meaning that there are multiple items in a given hash
                # table. otherwise the big O will be O(1) without collision, O(n) with collision
                for sub_bucket in bucket:
                    values_2.append(sub_bucket[1])

        print(values_2)


obj = HashTable(5)
print(obj)
obj.set('grapes', 1000)
obj.set('Grapes', 99999000)
obj.set('grapess', 21000)
print(obj)
obj.set('orange', 5000)
print(obj)
obj.set('apple', 2)
obj.set('applee', 200)
print(obj)
obj.set('Banana', 100)
print(obj)

obj.get('Grapes')

obj.keys()
obj.values()
obj.values_approach2()
