class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def initializeTree1():
    """
         10
         /\
        5  15
       /\  /\
      3 7 13 18
     /
    1
    """
    head = TreeNode(10)
    head.left = TreeNode(5)
    head.left.left = TreeNode(3)
    head.left.left.left = TreeNode(1)
    head.left.right = TreeNode(7)
    head.right = TreeNode(15)
    head.right.left = TreeNode(13)
    head.right.right = TreeNode(18)
    return head


def initializeTree2():
    """
         10
         /
        5
       /\
      4  7
     /    \
    1      8
    """
    head = TreeNode(10)
    head.left = TreeNode(5)
    head.left.left = TreeNode(4)
    head.left.left.left = TreeNode(1)
    head.left.right = TreeNode(7)
    head.left.right.right = TreeNode(8)
    return head


def initializeTreeGoogle():
    """
          1
         /\
        2  1
       /\  /\
      2 2 2  1
     /\  \   /\
    2  2  2 1  1
    """
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.left.left = TreeNode(2)
    head.left.left.left = TreeNode(2)
    head.left.left.right = TreeNode(2)
    head.left.right = TreeNode(2)
    head.left.right.right = TreeNode(2)
    head.right = TreeNode(1)
    head.right.left = TreeNode(2)
    head.right.right = TreeNode(1)
    head.right.right.left = TreeNode(1)
    head.right.right.right = TreeNode(1)
    return head


def InorderTraversalPrint(head):
    if not head:
        return None
    InorderTraversalPrint(head.left)
    print(head.val)
    InorderTraversalPrint(head.right)


def PreorderTraversalPrint(head):
    if not head:
        return None
    print(head.val)
    PreorderTraversalPrint(head.left)
    PreorderTraversalPrint(head.right)


def PostorderTraversalPrint(head):
    if not head:
        return None
    PostorderTraversalPrint(head.left)
    PostorderTraversalPrint(head.right)
    print(head.val)


def InorderTraversalIterative(head):
    current = head
    stack = []
    done = False
    while not done:
        if current:
            stack.append(current)
            current = current.left
        else:
            if len(stack) > 0:
                current = stack.pop()
                print(current.val)
                current = current.right
            else:
                done = True


def BFSIterativePrint(head):
    nodes = [head]
    while nodes:
        top = nodes.pop(0)
        print(top.val)
        if top.left:
            nodes.append(top.left)
        if top.right:
            nodes.append(top.right)


def DFSIterativePrint(head):
    if not head:
        return
    nodes = [head]
    while nodes:
        top = nodes.pop()
        print(top.val)
        if top.right:
            nodes.append(top.right)
        if top.left:
            nodes.append(top.left)


def DFSRecursivePrint(head):
    if not head:
        return None
    print(head.val)
    if head.left:
        DFSRecursivePrint(head.left)
    if head.right:
        DFSRecursivePrint(head.right)


def LevelPrintIterative(head):
    queue = [head]
    level = 1
    while True:
        if not len(queue):
            break
        print("Level:", level)
        temp = []
        while len(queue) != 0:
            top = queue.pop(0)
            print(top.val)
            if top.left:
                temp.append(top.left)
            if top.right:
                temp.append(top.right)
        queue = temp
        level += 1


def MaximumPathLengthRecursive(head):
    ans = [0]
    def helper(head):
        if not head:
            return 0
        l = helper(head.left)
        r = helper(head.right)
        ans[0] = max(ans[0], 1 + l + r)
        return 1 + max(l, r)
    helper(head)
    return ans[0]


def MaximumPathLabel(head):
    ans = [0]
    def helper(head):
        if not head:
            return 0, 1
        elif not head.left and not head.right:
            return 1, head.val
        l = helper(head.left)
        r = helper(head.right)
        if l[1] == r[1] and l[1] == head.val:
            # same label
            ans[0] = max(ans[0], 1 + l[0] + r[0])
            return 1 + max(l[0], r[0]), head.val
        elif l[1] == head.val:
            if l[0] >= r[0] - 1:
                ans[0] = max(ans[0], 1 + l[0])
            else:
                ans[0] = max(ans[0], r[0])
            return 1 + l[0], l[1]
        elif r[1] == head.val:
            if r[0] >= l[0] - 1:
                ans[0] = max(ans[0], 1 + r[0])
            else:
                ans[0] = max(ans[0], l[0])
            return 1 + r[0], r[1]
        else:
            if l[0] > r[0]:
                ans[0] = max(ans[0], l[0])
                return 1, head.val
            else:
                ans[0] = max(ans[0], r[0])
                return 1, head.val
    helper(head)
    return ans[0]


def MaximumPathSum(head):
    ans = [0]
    def helper(head):
        if not head:
            return 0
        if not head.left and not head.right:
            return head.val
        left = helper(head.left)
        right = helper(head.right)
        ans[0] = max(ans[0], head.val + left + right)
        if left > right:
            return head.val + left
        else:
            return head.val + right
    helper(head)
    return ans[0]


def TreePathSum(head, val):
    if not head or val - head.val < 0:
        return False
    if val - head.val == 0 and not head.left and not head.right:
        return True
    left = False; right = False
    if head.left:
        left = TreePathSum(head.left, val - head.val)
    if head.right:
        right = TreePathSum(head.right, val - head.val)
    return left or right


def TreeLeftView(head):
    current = head
    queue = [current]
    count = 1
    while len(queue) > 0:
        print(queue[0].val)
        nodes = 0
        while count > 0:
            top = queue.pop(0)
            count -= 1
            if top.left:
                queue.append(top.left)
                nodes += 1
            if top.right:
                queue.append(top.right)
                nodes += 1
        count = nodes


def TreeRightView(head):
    current = head
    queue = [current]
    count = 1
    while len(queue) > 0:
        nodes = 0
        while count > 0:
            top = queue.pop(0)
            if count == 1:
                print(top.val)
            count -= 1
            if top.left:
                queue.append(top.left)
                nodes += 1
            if top.right:
                queue.append(top.right)
                nodes += 1
        count = nodes


def main():
    # initialize tree
    t1 = initializeTree1()
    t2 = initializeTree2()
    tg = initializeTreeGoogle()

    # # Traversal and print
    # print("Inorder Traversal Recursive"); InorderTraversalPrint(t1); print()
    # print("Inorder Traversal Iterative"); InorderTraversalIterative(t1); print()
    # print("Preorder Traversal Recursive"); PreorderTraversalPrint(t1); print()
    # print("Postorder Traversal Recursive"); PostorderTraversalPrint(t1); print()

    # # Search Iterative and print
    # BFSIterativePrint(t1); print()
    # DFSIterativePrint(t1); print()

    # # Search Recursive and print
    # DFSRecursivePrint(t1); print()

    # # Print each level
    # LevelPrintIterative(t1); print()

    # # Tree path
    # print("Maximum Path Length Recursive t1"); print(MaximumPathLengthRecursive(t1)); print()
    # print("Maximum Path Length Recursive t2"); print(MaximumPathLengthRecursive(t2)); print()
    # print("Maximum Path Label"); print(MaximumPathLabel(tg)); print()
    # print("Maximum Path Sum Recursive"); print(MaximumPathSum(t2)); print()
    # print("Tree Path Sum Recursive"); print(TreePathSum(t1, 22)); print()

    # # Tree View
    # print("Tree Left View"); TreeLeftView(t1); print()
    # print("Tree Right View"); TreeRightView(t1); print()


if __name__ == "__main__":
    main()
