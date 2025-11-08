# DFS (recursive) and BFS for an undirected graph
# Simple adjacency-list representation, handles disconnected graphs

from collections import deque

def create_graph(n):
    """Create a graph with n vertices labeled 0..n-1."""
    return [[] for _ in range(n)]

def add_edge(adj, u, v):
    """Add undirected edge between u and v."""
    adj[u].append(v)
    adj[v].append(u)

def dfs(adj):
    """Perform DFS for entire graph (covers disconnected components).
       Returns list of vertices in the order they were visited."""
    n = len(adj)
    visited = [False] * n
    order = []

    def dfs_rec(node):
        visited[node] = True
        order.append(node)           # record visit
        for nbr in adj[node]:
            if not visited[nbr]:
                dfs_rec(nbr)         # recursive call

    # ensure every component is covered
    for v in range(n):
        if not visited[v]:
            dfs_rec(v)

    return order

def bfs(adj):
    """Perform BFS for entire graph (covers disconnected components).
       Returns list of vertices in the order they were visited."""
    n = len(adj)
    visited = [False] * n
    order = []

    for start in range(n):
        if visited[start]:
            continue
        q = deque([start])
        visited[start] = True
        while q:
            node = q.popleft()
            order.append(node)      # record visit
            for nbr in adj[node]:
                if not visited[nbr]:
                    visited[nbr] = True
                    q.append(nbr)
    return order



if __name__ == "__main__":
    # Create a graph with 7 nodes (0..6)
    adj = create_graph(7)
    edges = [
        (0, 1), (0, 2), (1, 3), (1, 4),
        (2, 5), (5, 6)  # this makes one component 0-1-3-4-2-5-6 (connected)
        # you can remove some edges to create disconnected components
    ]
    for u, v in edges:
        add_edge(adj, u, v)

    # Optional: sort adjacency lists so traversal order is predictable
    for lst in adj:
        lst.sort()

    print("Adjacency list:")
    for i, lst in enumerate(adj):
        print(f"{i}: {lst}")

    dfs_order = dfs(adj)
    bfs_order = bfs(adj)

    print("\nDFS (recursive) visit order:", dfs_order)
    print("BFS visit order:", bfs_order)
