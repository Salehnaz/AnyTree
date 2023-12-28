import random
from anytree import Node, RenderTree
from anytree.exporter import DotExporter

# Create the root node
root = Node("Root")

# Function to create a chain of nodes with 2-3 children per node and add random labels
def create_chain(node, level):
    if level < 10:
        num_children = random.randint(2, 3)  # Randomly assign 2 or 3 children
        children = []
        for i in range(num_children):
            child = Node(f"Child {level}_{i}", parent=node)
            label = random.choice(["UP", "DOWN", "BOTH"])
            child.label = label
            children.append(child)

        # Randomly choose one child to continue the chain
        chosen_child = random.choice(children)
        
        # Assign a random label (UP, DOWN, BOTH) to the edge
        label = random.choice(["UP", "DOWN", "BOTH"])
        chosen_child.label = label

        create_chain(chosen_child, level + 1)

# Create the chain structure
create_chain(root, 0)

# Visualize the tree using Graphviz with edge labels
def edge_label_func(parent, child):
    if hasattr(child, 'label'):
        return f'label="{child.label}"'
    else:
        return ''

DotExporter(root, edgeattrfunc=edge_label_func).to_picture("tree.png")

# Function to print relationships between nodes
def print_node_relationships(node):
    for pre, fill, sub_node in RenderTree(node):
        if sub_node.parent:
            print(f"{pre}({sub_node.parent.name}) --> ({sub_node.name})")

# Print relationships between nodes
print_node_relationships(root)
