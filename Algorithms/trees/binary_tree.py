from collections import deque

# Определяем структуру дерева
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Метод построения дерева из списка
def build_tree(values):
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        current = queue.popleft()

        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root

# Класс с методом обхода дерева
class Solution(object):
    def preorderTraversal(self, root):
        result = []

        def dfs(node):
            if not node:
                return
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return result

# Создаём дерево и вызываем метод
tree_list = [1, None, 2, 3]
root = build_tree(tree_list)

solution = Solution()  # Вот здесь создаётся объект Solution
print(solution.preorderTraversal(root))  # Выведет: [1, 2, 3]
