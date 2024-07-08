class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MyTree:
    def __init__(self, arr):
        last_f = (len(arr) // 2) - 1
        self.arr_tree = arr
        self.root = self.generate_sub_tree(arr, 0)

    def generate_sub_tree(self, arr, i):
        if i >= len(self.arr_tree) or arr[i] is None:
            return None

        node = TreeNode(val=arr[i])
        node.left = self.generate_sub_tree(arr, i * 2 + 1)
        node.right = self.generate_sub_tree(arr, i * 2 + 2)
        return node

    def print_inorder(self):
        r_list = self.inorder(self.root, [])
        print(r_list)

    def inorder(self, node: TreeNode, r_list):

        if node:
            if node.left:
                self.inorder(node.left, r_list)

            r_list.append(node.val)

            if node.right:
                self.inorder(node.right, r_list)

        return r_list


