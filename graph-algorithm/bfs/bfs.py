from collections import deque

def bfs(adj, start=0, target=None):
    """
    Perform BFS traversal on a graph.
    
    Args:
        adj: Adjacency list representation of the graph
        start: Starting node
        target: Target node to find path to (if None, performs full BFS traversal)
    
    Returns:
        If target is None: list of nodes in BFS traversal order
        If target is specified: path from start to target, or empty list if no path exists
    """
    # Handle both dictionary and list representations of adjacency list
    if isinstance(adj, dict):
        V = len(adj)
    else:
        V = len(adj)
    
    # For path tracking
    parent = {start: None}  # To reconstruct the path
    
    # For BFS traversal
    res = []
    q = deque()
    visited = [False] * V
    visited[start] = True
    q.append(start)
    
    while q:
        curr = q.popleft()
        res.append(curr)
        
        # If we found the target, reconstruct and return the path
        if target is not None and curr == target:
            path = []
            while curr is not None:
                path.append(curr)
                curr = parent.get(curr)
            return list(reversed(path))  # Return path from start to target
        
        # Process neighbors
        neighbors = adj[curr] if isinstance(adj, dict) else adj[curr]
        for i in neighbors:
            if not visited[i]:
                visited[i] = True
                parent[i] = curr  # Record the parent for path reconstruction
                q.append(i)
    
    # If target was specified but not found, return empty list
    if target is not None:
        return []
    
    # If no target specified, return the full traversal
    return res

if __name__ == "__main__":
    # Example usage
    # Adjacency list representation of a graph
    graph = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 5],
        3: [1],
        4: [1],
        5: [2]
    }
    
    # 1. Full BFS traversal starting from node 0
    print("Full BFS traversal:", bfs(graph))  # Output: [0, 1, 2, 3, 4, 5]
    
    # 2. Find path from node 0 to node 5
    path_0_to_5 = bfs(graph, start=0, target=5)
    print(f"Path from 0 to 5: {path_0_to_5}")  # Expected: [0, 2, 5]
    
    # 3. Find path from node 1 to node 5
    path_1_to_5 = bfs(graph, start=1, target=5)
    print(f"Path from 1 to 5: {path_1_to_5}")  # Expected: [1, 0, 2, 5]
    
    # 4. Find path to a node that doesn't exist or is unreachable
    path_0_to_6 = bfs(graph, start=0, target=6)
    print(f"Path from 0 to 6: {path_0_to_6}")  # Expected: [] (empty list, as node 6 doesn't exist)
    
    # Alternative: Using list representation instead of dictionary
    adj_list = [[1, 2], [0, 3, 4], [0, 5], [1], [1], [2]]
    print("Path using list format:", bfs(adj_list, start=0, target=3))  # Expected: [0, 1, 3]
