def update_tree(BITarray, length, position, value):
    position += 1

    while position <= length:
        BITarray[position] += value
        position += (position & -position)


class FenwickTree:
    def __init__(self, array):
        self.length = len(array) + 1
        self.BITarray = [0] * self.length
        self.construct_bit(array)

    def construct_bit(self, array):
        length = len(array)

        for i in range(0, length):
            update_tree(self.BITarray, self.length, i, array[i])

    def update_bit(self, position, value):
        position += 1

        while position < self.length:
            self.BITarray[position] += value
            position += (position & -position)

    def get_cu_freq(self, index):
        sum = 0
        while index > 0:
            sum += self.BITarray[index]
            index -= (index & -index)
        return sum

    def get_freq(self, index):
        value = self.BITarray[index]

        if index != 0:
            z = index - (index & -index)
            index -= 1
            while index != z:
                value -= self.BITarray[index]
                index -= (index & -index)

        return value

    def find_index_with_cu_freq(self, cu_freq):
        bit_mask = self._calculate_bit_mask()
        idx = 0
        max_idx = self.length - 1

        while bit_mask != 0:
            t_idx = idx + bit_mask
            bit_mask >>= 1

            if t_idx > max_idx:
                continue
            if cu_freq == self.BITarray[t_idx]:
                return t_idx
            elif cu_freq > self.BITarray[t_idx]:
                idx = t_idx
                cu_freq -= self.BITarray[t_idx]
        
        if cu_freq != 0:
            return -1
        else:
            return idx
    
    def _calculate_bit_mask(self):
        value = self.length - 1
        iter = 0
        while value != 0:
            value >>= 1
            iter += 1

        return pow(2, iter)


if __name__ == "__main__":
    array = [1, 0, 2, 1, 1, 3, 0, 4, 2, 5, 2, 2, 3, 1, 0, 2]
    sol = FenwickTree(array)
    print(sol.get_freq(16))
    print(sol.find_index_with_cu_freq(21))
