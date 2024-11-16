import networkx as nx
import random

class AntColonyGraphColoring:
    def __init__(self, graph, num_ants, alpha=1, beta=2, evaporation_rate=0.5, max_iterations=100):
        self.graph = graph
        self.num_ants = num_ants
        self.alpha = alpha  # Pheromone importance
        self.beta = beta  # Heuristic importance
        self.evaporation_rate = evaporation_rate
        self.max_iterations = max_iterations
        self.pheromone = {edge: 1 for edge in graph.edges}  # Initialize pheromones
    
    def heuristic(self, node, color, color_assignment):
        """Heuristic: Checks feasibility of color assignment."""
        for neighbor in self.graph.neighbors(node):
            if color_assignment.get(neighbor) == color:
                return 0  # Invalid if neighbor has the same color
        return 1  # Valid
    
    def color_graph(self):
        best_solution = None
        best_num_colors = float('inf')

        for iteration in range(self.max_iterations):
            solutions = []

            for _ in range(self.num_ants):
                color_assignment = {}
                for node in self.graph.nodes:
                    available_colors = []
                    for color in range(len(self.graph)):
                        if self.heuristic(node, color, color_assignment):
                            available_colors.append(color)

                    # Ant chooses color based on pheromone and heuristic
                    if available_colors:
                        probabilities = []
                        for color in available_colors:
                            # Calculate pheromone influence for the current color choice
                            pheromone_strength = 0
                            for neighbor in self.graph.neighbors(node):
                                if neighbor in color_assignment and color_assignment[neighbor] != color:
                                    pheromone_strength += self.pheromone.get((min(node, neighbor), max(node, neighbor)), 1)

                            # Adjust probability based on pheromone and heuristic
                            prob = (pheromone_strength ** self.alpha) * (1 ** self.beta)
                            probabilities.append(prob)

                        # Ensure we don't divide by zero by checking total_prob
                        total_prob = sum(probabilities)
                        if total_prob > 0:
                            probabilities = [p / total_prob for p in probabilities]
                            color = random.choices(available_colors, probabilities)[0]
                        else:
                            # If no pheromone influence, select a random color
                            color = random.choice(available_colors)

                        color_assignment[node] = color
                    else:
                        # If no available colors (shouldn't happen if heuristic is correct), assign a new color
                        color_assignment[node] = max(color_assignment.values(), default=0) + 1

                solutions.append(color_assignment)

            # Update pheromones based on solutions
            self._update_pheromones(solutions)

            # Check for the best solution
            for solution in solutions:
                num_colors = len(set(solution.values()))
                if num_colors < best_num_colors:
                    best_solution = solution
                    best_num_colors = num_colors

            print(f"Iteration {iteration + 1}: Best solution uses {best_num_colors} colors")

        return best_solution


    def _update_pheromones(self, solutions):
        # Evaporate existing pheromones
        for edge in self.pheromone:
            self.pheromone[edge] *= (1 - self.evaporation_rate)

        # Deposit new pheromones
        for solution in solutions:
            num_colors = len(set(solution.values()))
            for node, color in solution.items():
                for neighbor in self.graph.neighbors(node):
                    if solution[neighbor] != color:  # Valid edge
                        self.pheromone[(node, neighbor)] = self.pheromone.get((node, neighbor), 0) + (1 / num_colors)

# Example usage
if __name__ == "__main__":
    # Create a sample graph
    #G = nx.erdos_renyi_graph(10, 0.5, seed=42)  # 10 nodes, 50% connectivity
    
    G = nx.Graph()
    G.add_nodes_from(range(1, 17))
    G.add_edges_from([(1, 2), (1, 4), (1, 10), (2, 3), (2, 6), (2, 11), (2, 12), (2, 13), (3, 4), (3, 5), (3, 9), (5, 6), (6, 7), (6, 8), (8, 17), (10, 11), (11, 12), (12, 13), (12, 14), (13, 14), (14, 15), (15, 16)])

    
    colony = AntColonyGraphColoring(G, num_ants=10, max_iterations=50)
    solution = colony.color_graph()
    
    print("\nFinal Color Assignment:")
    for node, color in solution.items():
        print(f"Node {node}: Color {color}")
