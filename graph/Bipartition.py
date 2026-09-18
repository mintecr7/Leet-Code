def possible_bipartition(n: int, dislikes: list[list[int]]) -> bool:
    graph = [[] for _ in range(n + 1)]
    for a, b in dislikes:
        # print(a, b)
        # breakpoint()
        graph[a].append(b)
        graph[b].append(a)
    # print(graph)
    color = [0] * (n + 1)
    for i in range(1, n + 1):
        if color[i] == 0:
            color[i] = 1
            stack = [i]
            # print(stack)
            while stack:
                node = stack.pop()
                # print(node)
                for neighbor in graph[node]:
                    if color[neighbor] == color[node]:
                        return False
                    if color[neighbor] == 0:
                        color[neighbor] = 3 - color[node]
                        stack.append(neighbor)
                print(stack)
    # print(color)
    return True


a = possible_bipartition(
    10,
    [[5, 9], [5, 10], [5, 6], [5, 7], [1, 5], [4, 5], [2, 5], [5, 8], [3, 5]],
)
# print(a)
# print(is_cyclic(a))
