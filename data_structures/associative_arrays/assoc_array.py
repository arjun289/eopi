class AssocaitiveArray:
    def __init__(self, size=20):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def hash_function(self, key):
        sum = 0
        for pos in range(len(key)):
            sum = sum + ord(key[pos])

        return sum % self.size

    def put(self, key, value):
        index = self.hash_function(key)

        counter = 0
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value

            if counter > self.size:
                raise Exception('size', 'full')

            index = (index+1) % self.size
            counter += 1

        self.keys[index] = key
        self.values[index] = value
    
    def get(self, key):
        index = self.hash_function(key)

        counter = 0

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]

            index = (index+1) % self.size
            counter += 1
            if counter > self.size:
                return None

        return None


if __name__ == "__main__":
    test_hash = AssocaitiveArray()
    test_hash.put("car", 20)
    test_hash.put("car", 20)
    print(test_hash.get("car"))
