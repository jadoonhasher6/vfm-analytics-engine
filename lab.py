import heapq

def uniform_cost_search(graph, start, goal):
    priority_queue = [(0, start, [start])]
    visited = set()

    while priority_queue:
        
        (cost, current_node, path) = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        if current_node == goal:
            return cost, path

        visited.add(current_node)

        for neighbor, weight in graph.get(current_node, {}).items():
            if neighbor not in visited:
                total_cost = cost + weight
                heapq.heappush(priority_queue, (total_cost, neighbor, path + [neighbor]))

    return float("inf"), []

romania_map = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85}
}


total_distance, shortest_path = uniform_cost_search(romania_map, 'Arad', 'Bucharest')

print(f"Shortest distance from Arad to Bucharest: {total_distance} km")
print(f"Path: {' -> '.join(shortest_path)}")