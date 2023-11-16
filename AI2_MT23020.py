import pandas as pd
import heapq
import random

# Read data from CSV file
road_data = pd.read_csv('Road_Distance.csv')

road_data.columns = road_data.columns.str.lower()  # Convert column names to lowercase
road_data['distance in kilometres'] = road_data['distance in kilometres'].str.lower()  # Convert city names to lowercase

# Extract unique city names from the first column
cities = road_data.iloc[:, 0].tolist()

# print("Unique city names:", cities)




import networkx as nx
G = nx.Graph()

# Add nodes (cities) to the graph
for index, row in road_data.iterrows():
    city = row[0]
    for i in range(1, len(row)):
        if row[i] != '-' and row[i] != 0:
            G.add_edge(city, road_data.columns[i], distance=int(row[i]))



def uniform_cost_search(graph, start, goal):
    # Create a priority queue for storing nodes to be explored.
    # Each element in the queue is a tuple: (cumulative_cost, node)
    queue = [(0, start)]
    
    # Create a dictionary to keep track of the cumulative cost to reach each node.
    cumulative_costs = {node: float('inf') for node in graph.nodes}
    cumulative_costs[start] = 0
    
    # Create a dictionary to keep track of the parent node for each node.
    parents = {node: None for node in graph.nodes}
    
    while queue:
        # Get the node with the lowest cumulative cost from the priority queue.
        cumulative_cost, current_node = heapq.heappop(queue)
        
        # If we have reached the goal, reconstruct the path and return it.
        if current_node == goal:
            path = []
            while current_node is not None:
                path.insert(0, current_node)
                current_node = parents[current_node]
            return path
        
        # Explore the neighbors of the current node.
        for neighbor in graph.neighbors(current_node):
            # Calculate the cumulative cost to reach the neighbor through the current node.
            neighbor_cost = cumulative_cost + graph[current_node][neighbor]['distance']
            
            # If this cost is lower than the cost recorded for the neighbor so far, update it.
            if neighbor_cost < cumulative_costs[neighbor]:
                cumulative_costs[neighbor] = neighbor_cost
                parents[neighbor] = current_node
                # Add the neighbor to the priority queue with its cumulative cost.
                heapq.heappush(queue, (neighbor_cost, neighbor))
    
    # If the goal is not reachable from the start, return an empty path.
    return []




def heuristic_admissible(city, goal, road_map):
    path = uniform_cost_search(road_map, city, goal)
    cost = sum(G[path[i]][path[i+1]]['distance'] for i in range(len(path) - 1))
    cost -= 1500
    return cost



def heuristic_nonadmissible(city, goal, road_map):
    # Extract coordinates from the road_map dictionary
    path = uniform_cost_search(road_map, city, goal)
    cost = sum(G[path[i]][path[i+1]]['distance'] for i in range(len(path) - 1))
    random_penalty = random.randint(1000, 3000)
    cost += random_penalty
    return cost


def astar_search_admissible(graph, start, goal):
    # Create a priority queue for storing nodes to be explored.
    # Each element in the queue is a tuple: (total_cost, cumulative_cost, node)
    queue = [(heuristic_admissible(start, goal, graph), 0, start)]
    
    # Create a dictionary to keep track of the cumulative cost to reach each node.
    cumulative_costs = {node: float('inf') for node in graph.nodes}
    cumulative_costs[start] = 0
    
    # Create a dictionary to keep track of the parent node for each node.
    parents = {node: None for node in graph.nodes}
    
    while queue:
        # Get the node with the lowest total cost from the priority queue.
        total_cost, cumulative_cost, current_node = heapq.heappop(queue)
        
        # If we have reached the goal, reconstruct the path and return it along with the total cost.
        if current_node == goal:
            path = []
            while current_node is not None:
                path.insert(0, current_node)
                current_node = parents[current_node]
            return path, cumulative_costs[goal]  # Return both the path and the lowest cost
        
        # Explore the neighbors of the current node.
        for neighbor in graph.neighbors(current_node):
            # Calculate the cumulative cost to reach the neighbor through the current node.
            neighbor_cost = cumulative_cost + graph[current_node][neighbor]['distance']
            
            # If this cost is lower than the cost recorded for the neighbor so far, update it.
            if neighbor_cost < cumulative_costs[neighbor]:
                cumulative_costs[neighbor] = neighbor_cost
                parents[neighbor] = current_node
                # Add the neighbor to the priority queue with its total cost.
                total_cost = neighbor_cost + heuristic_admissible(neighbor, goal, graph)
                heapq.heappush(queue, (total_cost, neighbor_cost, neighbor))
    
    # If the goal is not reachable from the start, return an empty path and infinite cost.
    return [], float('inf')



def astar_search_nonadmissible(graph, start, goal):
    # Create a priority queue for storing nodes to be explored.
    # Each element in the queue is a tuple: (total_cost, cumulative_cost, node)
    queue = [(heuristic_nonadmissible(start, goal, graph), 0, start)]
    
    # Create a dictionary to keep track of the cumulative cost to reach each node.
    cumulative_costs = {node: float('inf') for node in graph.nodes}
    cumulative_costs[start] = 0
    
    # Create a dictionary to keep track of the parent node for each node.
    parents = {node: None for node in graph.nodes}
    
    while queue:
        # Get the node with the lowest total cost from the priority queue.
        total_cost, cumulative_cost, current_node = heapq.heappop(queue)
        
        # If we have reached the goal, reconstruct the path and return it along with the total cost.
        if current_node == goal:
            path = []
            while current_node is not None:
                path.insert(0, current_node)
                current_node = parents[current_node]
            return path, cumulative_costs[goal]  # Return both the path and the lowest cost
        
        # Explore the neighbors of the current node.
        for neighbor in graph.neighbors(current_node):
            # Calculate the cumulative cost to reach the neighbor through the current node.
            neighbor_cost = cumulative_cost + graph[current_node][neighbor]['distance']
            
            # If this cost is lower than the cost recorded for the neighbor so far, update it.
            if neighbor_cost < cumulative_costs[neighbor]:
                cumulative_costs[neighbor] = neighbor_cost
                parents[neighbor] = current_node
                # Add the neighbor to the priority queue with its total cost.
                total_cost = neighbor_cost + heuristic_nonadmissible(neighbor, goal, graph)
                heapq.heappush(queue, (total_cost, neighbor_cost, neighbor))
    
    # If the goal is not reachable from the start, return an empty path and infinite cost.
    return [], float('inf')







def main():

    start_city = input("Enter the starting city: ").lower()  # Convert input to lowercase
    end_city = input("Enter the destination city: ").lower()  # Convert input to lowercase

    if start_city not in cities:
        print("Start city not present in our dataset")
    elif end_city not in cities:
        print("End city not present in our dataset")
    else:
            # Uniform Cost Search
            ucs_path = uniform_cost_search(G, start_city, end_city)
            print("Uniform Cost Search Result:")
            print("Path:", ucs_path)
            total_cost = sum(G[ucs_path[i]][ucs_path[i+1]]['distance'] for i in range(len(ucs_path) - 1))
            print("Cost:", total_cost)

        
            # A* Search - Admissible Heuristic (Euclidean distance)
            astar_path_admissible, astar_cost_admissible = astar_search_admissible(G, start_city, end_city)
            print("A* Search (Admissible Heuristic - Euclidean) Result:")
            print("Path:", astar_path_admissible)
            print("Cost:", astar_cost_admissible)
            
            # A* Search - Non-Admissible Heuristic (Euclidean distance)
            astar_path_nonadmissible, astar_cost_nonadmissible = astar_search_nonadmissible(G, start_city, end_city)
            print("A* Search (Non-Admissible Heuristic - Euclidean) Result:")
            print("Path:", astar_path_nonadmissible)
            print("Cost:", astar_cost_nonadmissible)

if __name__ == "__main__":
    main()
