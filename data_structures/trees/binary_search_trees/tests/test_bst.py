from ..bst import BinarySearchTree


def test_bst_ops():
    my_tree = BinarySearchTree()
    my_tree.insert(10)
    my_tree.insert(5)
    my_tree.insert(15)

    assert my_tree.getMaxValue() == 15
    assert my_tree.getMinValue() == 5
