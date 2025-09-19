# 전위 순회한 값이 들어온다 => 결국 가장 먼저 값이 root라는 뜻.
import sys

sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 해제
input_value = sys.stdin.read().splitlines()

class Node():
    def __init__(self, value):
        self.root = value
        self.left = None
        self.right = None
    
    def insert(self, value):
        cur = self
        while True:
            if value < cur.root:
                if cur.left is None:
                    cur.left = Node(value)
                    return
                cur = cur.left
            elif value > cur.root:
                if cur.right is None:
                    cur.right = Node(value)
                    return
                cur = cur.right
            else:
                return

# 첫 번째 값이 root
root = Node(int(input_value[0]))
for i in input_value[1:]:
    root.insert(int(i))

def post_order(node):
    if node is not None:
        post_order(node.left)
        post_order(node.right)
        print(f"{node.root}")
        
post_order(root)