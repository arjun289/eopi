from ..queue_mod import Queue


def test_enqueue_op():
    my_qu = Queue()
    my_qu.enqueue(1)
    my_qu.enqueue(2)

    assert my_qu.queue == [1, 2]


def test_dequeu_op():
    my_qu = Queue()
    my_qu.enqueue(1)
    my_qu.enqueue(2)
    my_qu.enqueue(3)

    assert my_qu.dequeue() == 1
    assert my_qu.queue == [2, 3]


def test_peek():
    my_qu = Queue()
    my_qu.enqueue(1)
    my_qu.enqueue(2)
    my_qu.enqueue(3)

    assert my_qu.peek() == 1