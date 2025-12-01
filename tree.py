from __future__ import annotations
from typing import Generic, TypeVar, List, Optional, Callable

T = TypeVar("T")


class TreeNode(Generic[T]):
    def __init__(self, data: T, parent: Optional[TreeNode[T]] = None):
        self.data: T = data
        self.children: List[TreeNode[T]] = []
        self.parent: Optional[TreeNode[T]] = parent
        self.depth: int = 0 if parent is None else parent.depth + 1
        self.path: List[TreeNode[T]] = [] if parent is None else parent.path + [parent]

    def add_child(self, child_node: TreeNode[T]) -> None:
        child_node.parent = self
        child_node.depth = self.depth + 1
        child_node.path = self.path + [self]
        self.children.append(child_node)

    def __repr__(self, level: int = 0) -> str:
        ret = "\t" * level + repr(self.data) + "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret


def collect(
    node: TreeNode[T], predicate: Callable[[TreeNode[T]], bool]
) -> List[TreeNode[T]]:
    results: List[TreeNode[T]] = []

    if predicate(node):
        results.append(node)

    for child in node.children:
        results.extend(collect(child, predicate))

    return results
