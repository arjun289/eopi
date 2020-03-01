
class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        last_item = self.stack[-1]
        del self.stack[-1]
        return last_item

    def peek(self):
        return self.stack[-1]

    def stack_size(self):
        return len(self.stack)


if __name__ == "__main__":
    pass