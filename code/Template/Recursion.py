'''There is templates about recursion'''

'''

def recursion(level, param1, param2, ...):

    # recursion terminator
    if level > MAX_LEVEL:
        print_result
        return

    # process logic in current level
    process_data(level, data...)

    # drill down
    self.recursion(level + 1, p1, ...)

    # reverse the current level status if needed
    reverse_state(level)

'''

'''

visited = set()
def dfs(node, visited):
    visited.add(node)
    # process current node here.
    # ...
    for next_node in node.children():
        if not next_node in visited:
            dfs(next_node, visited)

'''

'''

def bfs(graph, start, end):

    queue = []
    queue.append([start])
    visited.add(start)

    while queue:
        node = queue.pop()
        visited.add(node)

        process(node)
        nodes = generate_related_nodes(node)
        queue.push(nodes)

    # other processing work
    # ...

'''