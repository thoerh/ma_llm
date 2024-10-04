# here are the classes defined which should stay the same for all surgeries like the:
#       Process class definition
#       Model for surgical simulation  
#       Defining scene defining variables      

# later
#       Scene graph class



import random



class GlobalVariables:
    def __init__(self, hygiene: float, skill_level: float, patient_health: float):
        self.hygiene = hygiene
        self.skill_level = skill_level
        self.patient_health = patient_health


class Process:
    def __init__(self, name, duration):
        self.name = name
        self.base_transitions = {}
        self.duration = duration
        
        self.adjustment_factors = {}

    def add_transition(self, next_process, base_probability):
        if not 0 <= base_probability <= 1:
            raise ValueError("base_probability must be between 0 and 1")
        self.base_transitions[next_process] = base_probability
        
        self.adjustment_factors[next_process] = 1.0  # Default factor



#for more complex prbobailities with the incorporation of the global variables
    def set_adjustment_factor(self, next_process, factor):
        if next_process not in self.adjustment_factors:
            raise ValueError(f"Adjustment factor for '{next_process}' not found. "
                             "Make sure the process has been added as a transition.")
        if factor < 0:
            raise ValueError(f"Adjustment factor must be non-negative, got {factor}")
        self.adjustment_factors[next_process] = factor

    def adjust_probabilities(self, global_vars):
        # Adjust probabilities based on global variables
        adjusted_transitions = {}
        for next_process, base_prob in self.base_transitions.items():
            factor = self.calculate_adjustment_factor(next_process, global_vars)
            adjusted_prob = base_prob * factor
            adjusted_transitions[next_process] = adjusted_prob
        # Normalize probabilities
        total = sum(adjusted_transitions.values())
        return {proc: prob / total for proc, prob in adjusted_transitions.items()}
    
    def calculate_adjustment_factor(self, next_process, global_vars):
        # This method determines how global variables affect the transition
        factor = self.adjustment_factors[next_process]

        # Example adjustments:
        if "complication" in next_process.name.lower():
            factor *= (1 - global_vars.hygiene)  # Lower hygiene increases complication probability
        if "success" in next_process.name.lower():
            factor *= global_vars.skill_level  # Higher skill level increases success probability

        return factor




    def get_next_process(self, global_vars):
        adjusted_probs = self.adjust_probabilities(global_vars)
        
        r = random.random()  # Random float between 0 and 1
        cumulative_probability = 0.0
        for next_process, probability in adjusted_probs.items():
            cumulative_probability += probability
            if r < cumulative_probability:
                return next_process
        return None  # In case no transition occurs (error handling)
    
   




        
class SurgicalSimulation:
    def __init__(self, GlobalVariables: str):
        self.global_vars = GlobalVariables

    #def set_start_process(self, process):
    #    self.current_process = process

    def run(self, current_process: str):
        self.current_process = current_process
        print(f"Starting process: {self.current_process.name}")
        while self.current_process is not None:
            print(f"Executing process: {self.current_process.name} (Duration: {self.current_process.duration})")
            next_process = self.current_process.get_next_process(self.global_vars)
            if next_process:
                print(f"Transitioning to: {next_process.name}")
                self.current_process = next_process
            else:
                print("End of surgery.")
                self.current_process = None

    # Simulate a simple surgery
    #def run(self, current_process: str):
        #self.current_process = current.process
        #while self.current_process:
            #print(f"Current process: {self.current_process.name} (Duration: {self.current_process.duration})")
            #current_process = current_process.get_next_process(self.global_vars)
        #print("Surgery completed.")