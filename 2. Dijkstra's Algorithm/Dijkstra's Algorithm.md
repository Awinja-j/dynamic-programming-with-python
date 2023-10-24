## Dijkstra's algorithm 

is a graph search algorithm used to find the shortest path from a source node to all other nodes in a weighted graph. It's commonly used in applications like routing and network design. Here's an overview of how the algorithm works:

**Input**:
1. A weighted graph, where each edge has a non-negative weight.
2. A source node from which you want to find the shortest paths to all other nodes in the graph.

**Output**:
1. The shortest distance from the source node to all other nodes.
2. The shortest path from the source node to all other nodes.

**Algorithm Steps**:

1. **Initialization**:
   - Create a set of unvisited nodes.
   - Assign a tentative distance value to every node. Set the distance to the source node as 0 and all other nodes as infinity. You'll use this value to keep track of the shortest distance found so far.

2. **Select the Node with the Shortest Distance**:
   - While there are unvisited nodes, select the node with the smallest tentative distance as the current node.
   - Initially, this will be the source node with a distance of 0.

3. **Explore Neighbors**:
   - For the current node, consider all of its neighbors (nodes connected by an edge).
   - Calculate their tentative distances through the current node. If this new tentative distance is less than their current assigned value, update the node's distance.

4. **Mark Current Node as Visited**:
   - After considering all the neighbors of the current node, mark the current node as visited. A visited node will not be checked again.

5. **Repeat Steps 2-4**:
   - Repeat steps 2-4 until you have visited all nodes or, if there is no path from the source node to a node, the tentative distance remains infinity.

6. **Path Reconstruction**:
   - Once you have determined the shortest distances to all nodes, you can reconstruct the shortest path from the source node to any other node by backtracking from the destination node to the source node, following the node with the smallest tentative distance.

**Key Points**:

- Dijkstra's algorithm is suitable for graphs with non-negative edge weights. It doesn't work correctly if the graph has negative edge weights.

- It guarantees the shortest path when all edge weights are non-negative.

- Dijkstra's algorithm can be implemented using various data structures like a priority queue (heap) to improve its efficiency, especially when dealing with large graphs.

- The time complexity of Dijkstra's algorithm is O(V^2) without using a priority queue and O((E + V) * log(V)) with a priority queue, where V is the number of vertices and E is the number of edges.

Dijkstra's algorithm is a fundamental tool in graph theory and network optimization and is widely used in computer science and various real-world applications such as GPS navigation and network routing protocols.