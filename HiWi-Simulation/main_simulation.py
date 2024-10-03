print("Let's go")

class SceneGraph:
    def __init__(self, nodes, positions, timestamp):
        self.nodes = nodes
        self.positions = positions
        self.timestamp = timestamp

class Process:
    def __init__(self, process_name, scene_graphs):
        self.process_name = process_name  # Name of the process, e.g., 'cleaning'
        self.scene_graphs = scene_graphs  # List of scene graphs related to this process

    def get_duration(self):
        # Return the time duration of this process based on the timestamps of the scene graphs
        if self.scene_graphs:
            start_time = self.scene_graphs[0].timestamp
            end_time = self.scene_graphs[-1].timestamp
            return end_time - start_time
        return 0

    def get_spatial_relationships(self):
        # Optionally: return spatial relationships of nodes across the scene graphs
        return [graph.positions for graph in self.scene_graphs]

class SurgerySimulation:
    def __init__(self, initial_graph, global_vars):
        self.current_graph = initial_graph
        self.global_vars = global_vars
    
    def transition(self, current_process):
        # Use probabilities and global variables to determine the next process
        pass
    
    def run(self):
        while not self.end_of_surgery():
            next_process = self.transition(self.current_process)
            self.update_scene_graph(next_process)
    
    def update_scene_graph(self, process):
        # Update the scene graph based on the process
        pass



# Initialize and run
global_vars = {'surgeon_skill': 0.9, 'hygiene_level': 0.8}
initial_graph = SceneGraph(nodes, positions, timestamp)
simulation = SurgerySimulation(initial_graph, global_vars)
simulation.run()