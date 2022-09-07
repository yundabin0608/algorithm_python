# 트리 순회

# 이진 트리를 입력받아 전위순회, 중위순회, 후위순회한 결과 출력

import sys
input = sys.stdin.readline

class Node:
  def __init__(self, data, left, right):
    self.data = data
    self.left = left
    self.right = right

def preorder(n):
    print(n.data, end="")
    if n.left != '.': preorder(tree[n.left])
    if n.right != '.': preorder(tree[n.right])

def inorder(n):
    if n.left != '.': inorder(tree[n.left])
    print(n.data, end="")
    if n.right != '.': inorder(tree[n.right])

def postorder(n):
    if n.left != '.': postorder(tree[n.left])
    if n.right != '.': postorder(tree[n.right])
    print(n.data, end="")

tree = {}
for _ in range(int(input())):
    node, left, right = input().split()
    tree[node] = Node(data=node, left=left, right=right)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])