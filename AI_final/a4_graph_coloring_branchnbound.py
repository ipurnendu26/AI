def is_safe(vertex, graph, color, c):
    for neighbor in graph[vertex]:
        if color[neighbor] == c:
            return False
    return True

def graph_coloring(graph, colors, vertex, color):
    if vertex == len(graph):
        return True

    for c in colors:
        if is_safe(vertex, graph, color, c):
            color[vertex] = c
            if graph_coloring(graph, colors, vertex + 1, color):
                return True
            color[vertex] = None

    return False

def solve_graph_coloring(graph, colors):
    color = [None] * len(graph)
    if graph_coloring(graph, colors, 1, color):
        return color
    return None

# Example usage
graph = {
    1: [3, 2],
    2: [ 1, 4, 5],
    3: [1, 4],
    4: [2, 5, 3]
}

colors = ['red', 'green', 'blue']
solution = solve_graph_coloring(graph, colors)

if solution:
    for vertex, c in enumerate(solution):
        print(f"Vertex {vertex} is colored {c}")
else:
    print("No valid coloring found.")
