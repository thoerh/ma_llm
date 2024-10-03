# here are the classes defined which should stay the same for all surgeries like the:
#       Process class definition
#       Model for surgical simulation  
#       Defining scene defining variables      

# later
#       Scene graph class



import random

class Process:
    def __init__(self, name):
        self.name = name
        self.transitions = []

    def add_transition(self, next_process, probability):
        self.transitions.append((next_process, probability))

    def get_next_process(self):
        r = random.random()  # Random float between 0 and 1
        cumulative_probability = 0.0
        for next_process, probability in self.transitions:
            cumulative_probability += probability
            if r < cumulative_probability:
                return next_process
        return None  # In case no transition occurs (error handling)

class SurgicalSimulation:
    def __init__(self):
        self.current_process = None

    def set_start_process(self, process):
        self.current_process = process

    def run(self):
        print(f"Starting process: {self.current_process.name}")
        while self.current_process is not None:
            next_process = self.current_process.get_next_process()
            if next_process:
                print(f"Transitioning to: {next_process.name}")
                self.current_process = next_process
            else:
                print("End of surgery.")
                self.current_process = None