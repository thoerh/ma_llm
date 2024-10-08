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
    def __init__(self, Processname, Duration: float):
        self.name = Processname
        self.base_transitions = {}
        self.duration = Duration
        
        self.adjustment_factors = {}
        self.adjustable_transitions = set()


    def add_transition(self, next_process, base_probability: float):
        if not 0 <= base_probability <= 1:
            raise ValueError("base_probability must be between 0 and 1")
        self.base_transitions[next_process] = base_probability
        self.adjustment_factors[next_process] = 1.0  # Default factor
        self.adjustable_transitions.add(next_process)

    def add_alt_transition(self, next_process, base_probability: float):
        if not 0 <= base_probability <= 1:
            raise ValueError("base_probability must be between 0 and 1")
        self.base_transitions[next_process] = base_probability
        
    def add_redo_transition(self, base_probability):
        if not 0 <= base_probability <= 1:
            raise ValueError("base_probability must be between 0 and 1")
        next_process = self.name
        self.base_transitions[next_process] = base_probability



#for more complex probabilities with the incorporation of the global variables
    def set_adjustment_factor(self, next_process, factor):
        if next_process not in self.adjustment_factors:
            raise ValueError(f"Adjustment factor for '{next_process}' not found. "
                             "Make sure the process has been added as a transition.")
        if factor < 0:
            raise ValueError(f"Adjustment factor must be non-negative, got {factor}")
        self.adjustment_factors[next_process] = factor



    def calculate_adjustment_factor(self, next_process, global_vars):
        # This method determines how global variables affect the transition
        factor = self.adjustment_factors[next_process]

        # Example adjustments:
        if global_vars.hygiene < 0.6:
            factor *= (global_vars.hygiene)  # Lower hygiene increases complication/redo probability and decreases progress probability
        if global_vars.skill_level < 0.6:
            factor *= global_vars.skill_level  # Lower skill level decreases progress probability
        if global_vars.patient_health < 0.6:
            factor *= global_vars.patient_health  # Lower patient_health decreases progress probability

        return factor
    


    def adjust_probabilities(self, global_vars):
        # Adjust probabilities based on global variables
        adjusted_transitions = {}
        unadjusted_transitions = {}
        adjusted_sum = 0
        unadjusted_sum = 0
        for next_process, base_prob in self.base_transitions.items():
            if next_process in self.adjustable_transitions:
                factor = self.calculate_adjustment_factor(next_process, global_vars)
                adjusted_prob = base_prob * factor
                adjusted_transitions[next_process] = adjusted_prob
                adjusted_sum += adjusted_prob
            else:
                unadjusted_transitions[next_process] = base_prob
                unadjusted_sum += base_prob

        total_probability = adjusted_sum + unadjusted_sum
            
            
        if total_probability < 1:
            # Increase unadjusted probabilities to make the total sum 1
            scale_factor = (1 - adjusted_sum) / unadjusted_sum if unadjusted_sum > 0 else 1
            for next_process, prob in unadjusted_transitions.items():
                unadjusted_transitions[next_process] = prob * scale_factor
        elif total_probability > 1:
            # Scale down all probabilities proportionally
            scale_factor = 1 / total_probability
            for next_process in self.base_transitions:
                if next_process in adjusted_transitions:
                    adjusted_transitions[next_process] *= scale_factor
                else:
                    unadjusted_transitions[next_process] *= scale_factor

        # Combine adjusted and unadjusted transitions
        final_transitions = {**adjusted_transitions, **unadjusted_transitions}

        return final_transitions




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
    def __init__(self, GlobalVariables):
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