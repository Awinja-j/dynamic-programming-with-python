def dijkstra_solution(unvisited_nodes, edges, source_node):
    path_lengths = {v : float('inf') for v in unvisited_nodes} #{1: inf, 2: inf, 3: inf, 4: inf, 5: inf, 6: inf}

    path_lengths[source_node] = 0 #{1: inf, 2: inf, 3: inf, 4: inf, 5: inf, 6: inf, 0: 0}

    adjacent_nodes = { v:{} for v in unvisited_nodes} # {1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}}

    for (u,v), w_uv in edges.items():
        # u,v,w_uv is 0 1 1.0
        adjacent_nodes[u][v] = w_uv
        adjacent_nodes[v][u] = w_uv

    temporary_nodes = [v for v in unvisited_nodes]
    while len(temporary_nodes) > 0:
        upper_bounds = {v: path_lengths[v] for v in temporary_nodes}
        u = min(upper_bounds, key=upper_bounds.get)

        temporary_nodes.remove(u)

        for v, w_uv in adjacent_nodes[u].items():
            path_lengths[v] = min(path_lengths[v], path_lengths[u] + w_uv)

    return path_lengths


result = dijkstra_solution([0,1,2,3,4,5],{(0,1): 1.0, (0,2): 1.5, (0,3): 2.0, (1,3): 0.5, (1,4):2.5, (2,3): 1.5, (3,5): 1.0}, 0 )
print(result)