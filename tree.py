class Node:
    def __init__(self, key: int):
        self._key = key
        self._left = None
        self._right = None

    @property
    def key(self) -> int:
        return self._key

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, value):
        if self.left is not None:
            raise NotImplementedError
        self._left = value

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, value):
        if self.right is not None:
            raise NotImplementedError
        self._right = value


class BinaryTree:
    def __init__(self, root: Node):
        self._root = root

    def add(self, node: Node) -> None:
        _add_recursive(parent=self._root, new_node=node)


def _add_recursive(parent: Node, new_node: Node) -> None:
    def _set_or_add(side: str) -> None:
        node = getattr(parent, side)
        if node is None:
            setattr(parent, side, new_node)
        else:
            _add_recursive(parent=node, new_node=new_node)

    if new_node.key <= parent.key:
        _set_or_add(side='left')
    else:
        _set_or_add(side='right')
