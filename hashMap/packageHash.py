"""
A hash map is created.
Citation: Joe James. (2016, January 22). Python: Creating a HASHMAP using Lists.[Video]. YouTube.
	            https://www.youtube.com/watch?v=9HFbhPscPU0
"""
class packageHash:
    def __init__(self):
        """
        The hash map is initialized using buckets.  By default, 64 are created.
        O(1)
        """
        self.size = 64
        self.map = [None] * self.size
    def _get_hash(self, key):
        """
        The hash key is created.  Since each package has a unique id, the hash is created using the package id % 10.
        This is a very basic hash function, but it is all that is needed for 40 packages. O(1)
        :param key: A package id is used as the key
        :return: the function returns a 'hash' as the unique identifier.
        """
        hash = 0
        hash = int(key)
        hash = hash % 10
        return hash

    def add(self, key, value):
        """
        This is my insertion function into the hash map.
        The function adds a function to the hashmap.  The function calls the _get_hash function to get the hash key
        and uses this to store the value.
        Time complexity O(n)
        Space complexity O(n)
        :param key: Key is the unique identifier
        :param value: value is what is being added to the hash
        :return: returns true
        """
        key_hash = self._get_hash(key)
        key_value = [key,value]

        if(self.map[key_hash] is None):
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
                self.map[key_hash].append(key_value)
                return True

    def get(self, key):
        """
        The function uses a key and the _get_hash function to find and return a value from the hash map.  If no value
        is found, nothing is returned.
        Space complexity O(n)
        Time complexity O(n)
        :param key: Key is the unique identifer
        :return: returns value or none
        """
        key_hash = self._get_hash(int(key))
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        """
        The function uses a key and the _get_hash function to find and delete a value from the hash map.  If no value
        is found, false is returned.
        Space complexity O(n)
        Time complexity O(n)
        :param key: Key is the unique identifier
        :return: true or false
        """
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            return False
        for i in range (0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

