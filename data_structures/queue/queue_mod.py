class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]

        return data

    def peek(self):
        return self.queue[0]

    def sizeQueue(self):
        return len(self.queue)
