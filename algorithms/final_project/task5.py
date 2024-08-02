import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


class Node:
    def __init__(self, key, color="#000000"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(
            node.id, color=node.color, label=node.val
        )  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, step_delay=0.5):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {
        node[0]: node[1]["label"] for node in tree.nodes(data=True)
    }  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()
    plt.pause(step_delay)


def array_to_bst(arr, i=0):
    if i >= len(arr) or arr[i] is None:
        return None
    root = Node(arr[i])
    root.left = array_to_bst(arr, 2 * i + 1)
    root.right = array_to_bst(arr, 2 * i + 2)
    return root


def get_color(index, total_steps):
    hue = index / total_steps
    lightness = 0.5 + 0.5 * (index / total_steps)
    return mcolors.hsv_to_rgb((hue, 1, lightness))


def bfs(root):
    if root is None:
        return
    queue = [root]
    step = 0
    while queue:
        current = queue.pop(0)
        current.color = mcolors.to_hex(get_color(step, total_steps=15))
        step += 1
        draw_tree(root)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)


def dfs(root):
    if root is None:
        return
    stack = [root]
    step = 0
    while stack:
        current = stack.pop()
        current.color = mcolors.to_hex(get_color(step, total_steps=15))
        step += 1
        draw_tree(root)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)


# Приклад бінарної купи у вигляді масиву
heap = [0, 1, 4, 3, 5, 10]

# Перетворення масиву на дерево
root = array_to_bst(heap)

# Відображення обходу в ширину (BFS)
print("Breadth-First Search (BFS):")
bfs(root)

# Відображення обходу в глибину (DFS)
print("Depth-First Search (DFS):")
root = array_to_bst(heap)  # Перетворення масиву на дерево знову, щоб скинути кольори
dfs(root)
