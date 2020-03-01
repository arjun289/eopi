from ..stack_mod import Stack


def test_my_stack_push():
    my_stack = Stack()
    my_stack.push(1)
    assert my_stack.stack == [1]


def test_my_stack_pop():
    my_stack = Stack()
    my_stack.push(1)
    my_stack.push(2)

    assert my_stack.pop() == 2
    assert my_stack.stack == [1]


def test_stack_peek():
    my_stack = Stack()
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)

    assert my_stack.peek() == 3 
