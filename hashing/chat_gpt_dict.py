class Dictionary:

    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size  # stores keys
        self.data = [None] * self.size   # stores values

    def hash_func(self, key):
        return abs(hash(key)) % self.size

    def put(self, key, value):
        hash_val = self.hash_func(key)

        if self.slots[hash_val] is None:
            self.slots[hash_val] = key
            self.data[hash_val] = value  # ✅ fix here
        else:
            if self.slots[hash_val] == key:
                self.data[hash_val] = value
            else:
                new_hash_val = self.rehash(hash_val)
                while self.slots[new_hash_val] is not None and self.slots[new_hash_val] != key:
                    new_hash_val = self.rehash(new_hash_val)

                if self.slots[new_hash_val] is None:
                    self.slots[new_hash_val] = key
                    self.data[new_hash_val] = value
                else:
                    self.data[new_hash_val] = value

    def rehash(self, old_hash):
        return (old_hash + 1) % self.size

# Example usage
d1 = Dictionary(3)
d1.put('python', 100)
d1.put('java', 10)

print(d1.slots)
print(d1.data)
