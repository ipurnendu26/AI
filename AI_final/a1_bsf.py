from queue import Queue

# Breadth-First Search (BFS)
def bfs(graph, start):
    visited = []
    queue = Queue()
    queue.put(start)
    visited.append(start)

    while not queue.empty():
        vertex = queue.get()
        print(f"Processing {vertex}");  # Process the vertex

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.put(neighbor)
                visited.append(neighbor)
        print(f"Visited: {visited}")
        print(f"Queue contents: {queue.queue}");


# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("BFS traversal:")
bfs(graph, 'A')

