# here are the classes defined which should stay the same for all surgeries like the:
#       Defining class for scene defining variables
#       Process class definition
#       Model for surgical simulation  
      

# later
#       Scene graph class
#       incorporate timing



import random
from object_classes import Object
from scipy import stats
import math




class GlobalVariables:
    def __init__(self, hygiene: float, skill_level: float, patient_health: float):
        self.hygiene = hygiene
        self.skill_level = skill_level
        self.patient_health = patient_health


class Transition:
    def __init__(self, from_process, to_process):
        self.from_process = from_process
        self.to_process = to_process
        self.moving_objects = {}

    def calculate_distance(self, pos1, pos2):
        return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

    def calculate_move_time(self, object, start_pos, end_pos, speed=1.0):
        distance = self.calculate_distance(start_pos, end_pos)
        return distance / speed

    def prepare_transition(self):
        for obj, attrs in self.to_process.objects.items():
            if 'position' in attrs:
                start_pos = self.from_process.objects[obj]['position'] if obj in self.from_process.objects else obj.position
                end_pos = attrs['position']
                move_time = self.calculate_move_time(obj, start_pos, end_pos)
                self.moving_objects[obj] = {
                    'start_pos': start_pos,
                    'end_pos': end_pos,
                    'move_time': move_time 
                }

    def execute_transition(self, elapsed_time):
        still_moving = False
        for obj, move_info in self.moving_objects.items():
            if elapsed_time < move_info['move_time']:
                progress = elapsed_time / move_info['move_time']
                new_pos = (
                    move_info['start_pos'][0] + (move_info['end_pos'][0] - move_info['start_pos'][0]) * progress,
                    move_info['start_pos'][1] + (move_info['end_pos'][1] - move_info['start_pos'][1]) * progress
                )
                obj.position = new_pos
                print(f"Moving (t: {elapsed_time:.2f}): {obj.name:<25} from {self.from_process.name:<15} Position {move_info['start_pos']} -> {self.to_process.name:<15} Position {move_info['end_pos']} => {obj.position}")
                still_moving = True
            else:
                obj.position = move_info['end_pos']
                print(f"Arrived: {obj.name} at {self.to_process.name} Position => {obj.position}")
        return still_moving
    



class Process:
    def __init__(self, Processname, mean_duration: float, base_variance: float):
        self.name = Processname
        self.base_transitions = {}
        self.objects = {}

        self.adjustment_factors = {}
        self.adjustable_transitions = set()

        self.transitions = {}
        self.time = Time(self, mean_duration, base_variance)
        
        

    def print_process_dictionary (self, dictionary):
        def convert_to_str(value):
            if isinstance(value, list):
                return [str(item) for item in value]
            return str(value)
        
         # Define the width for the fields you want to align
        role_width = 13  # Set a fixed width for the role
        name_width = 20  # Set a fixed width for the name
        
        for object, attributes in dictionary.items():
            str_attributes = {k: convert_to_str(v) for k, v in attributes.items()}
            print(f"Process {self.name}    Object: {object.role:<{role_width}} - {object.name:<{name_width}}      ->     Attributes: {str_attributes}")
    
    
    def print_dictionaries(self, dictionary1, dictionary2):
        for (process1, prob1), (process2, prob2) in zip(dictionary1.items(), dictionary2.items()):
            print(f"Transition: {self.name:<35} -> {process1.name:<35},     Base Probability: {prob1:<5},      adjusted: {prob2}")


    def add_object_attribute(self, object, attributes):
        self.objects [object]= attributes
        for attr, value in attributes.items():
            if hasattr(object, attr):
                setattr(object, attr, value)

    def add_transition(self, next_process, base_probability: float):
        if not 0 <= base_probability <= 1:
            raise ValueError("base_probability must be between 0 and 1")
        self.base_transitions[next_process] = base_probability
        self.adjustment_factors[next_process] = 1.0  # Default factor
        self.adjustable_transitions.add(next_process)
        self.transitions[next_process] = Transition(self, next_process)

    def add_alt_transition(self, next_process, base_probability: float):
        if not 0 <= base_probability <= 1:
            raise ValueError("base_probability must be between 0 and 1")
        self.base_transitions[next_process] = base_probability
        self.transitions[next_process] = Transition(self, next_process)
        
    def add_redo_transition(self, base_probability):
        if not 0 <= base_probability <= 1:
            raise ValueError("base_probability must be between 0 and 1")
        next_process = self
        self.base_transitions[next_process] = base_probability
        self.transitions[next_process] = Transition(self, next_process)



#for more complex probabilities with the incorporation of the global variables
    def set_adjustment_factor(self, next_process, factor):
        if next_process not in self.adjustment_factors:
            raise ValueError(f"Adjustment factor for '{next_process}' not found. "
                             "Make sure the process has been added as a transition.")
        if factor < 0:
            raise ValueError(f"Adjustment factor must be non-negative, got {factor}")
        self.adjustment_factors[next_process] = factor



    def calculate_adjustment_factor(self, next_process, global_vars):        # This method determines how global variables affect the transition
        factor = self.adjustment_factors[next_process]

        # Example adjustments:
        if global_vars.hygiene < 0.6:
            factor *= global_vars.hygiene  # Lower hygiene increases complication/redo probability and decreases progress probability
        if global_vars.skill_level < 0.6:
            factor *= global_vars.skill_level  # Lower skill level decreases progress probability
        if global_vars.patient_health < 0.6:
            factor *= global_vars.patient_health  # Lower patient_health decreases progress probability

        return factor
    


    def adjust_probabilities(self, global_vars):         # Adjust probabilities based on global variables
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
        adjusted_dict = dict(sorted(adjusted_probs.items(), key=lambda item: item[1], reverse=False))
        
        r = random.random()  # Random float between 0 and 1
        print(f"Random value: {r}")
        self.print_dictionaries(self.base_transitions, adjusted_probs)
       
        cumulative_probability = 0.0
        for next_process, probability in adjusted_dict.items():
            cumulative_probability += probability
            if r < cumulative_probability:
                return next_process
        return None  # In case no transition occurs (error handling)
    
   



class Time:
    def __init__(self, process, mean, base_variance):
        self.process = process
        self.mean = mean
        self.base_variance = base_variance

    def calculate_adjusted_variance(self, global_vars):
        # Adjust variance based on skill level
        skill_factor = 1 + (1 - global_vars.skill_level)  # Higher skill reduces variance
        # Adjust variance based on patient health
        health_factor = 1 + (1 - global_vars.patient_health)  # Better health reduces variance
        
        return self.base_variance * skill_factor * health_factor

    def get_time(self, global_vars):
        adjusted_variance = self.calculate_adjusted_variance(global_vars)
        
        # Generate time using a normal distribution and the adapted variance
        time = stats.truncnorm(
            (0 - self.mean) / adjusted_variance,
            (float('inf') - self.mean) / adjusted_variance,
            loc=self.mean,
            scale=adjusted_variance
            ).rvs()
        
        return max(0, time)  # Ensure non-negative time
    

        

class SurgicalSimulation:
    def __init__(self, GlobalVariables):
        self.global_vars = GlobalVariables
        self.history = []
        self.current_process = None
        self.total_time = 0
        self.transition_time = 0

    def run(self, starting_process):
        self.current_process = starting_process
        print(f"\nStarting process: {self.current_process.name}")

        while self.current_process is not None:
            process_time = self.current_process.time.get_time(self.global_vars)
            self.total_time += process_time
            print(f"Executing process: {self.current_process.name} (Duration: {process_time:.2f})")
            self.current_process.print_process_dictionary(self.current_process.objects)
            self.history.append((self.current_process.name, process_time))

            next_process = self.current_process.get_next_process(self.global_vars)

            if next_process is None:
                print("\nEnd of surgery.\n")
                self.current_process = None
            elif next_process.name == 'Error':
                print("An error occurred in the surgery. Ending simulation.\n")
                self.current_process = None
            else:
                print(f"Transitioning to: {next_process.name}\n")
                
                # Check if transition exists
                if next_process in self.current_process.transitions:
                    transition = self.current_process.transitions[next_process]
                    transition.prepare_transition()
                    
                    # Execute transition
                    elapsed_time = 0
                    #objects_still_moving = True
                    while transition.execute_transition(elapsed_time):                                      ##############Maybe back to objects_still_moving (look in claudeai)
                        elapsed_time += 0.1  # Simulate time steps
                        self.transition_time += 0.1
                        self.total_time += 0.1
                        ##objects_still_moving = transition.execute_transition(elapsed_time)
                        ##print("Moving objects:", transition.moving_objects)             ################################
                    
                    print(f"Transition completed. Time taken: {elapsed_time:.2f}\n")
                    self.current_process = next_process
                else:
                    print(f"No transition defined from {self.current_process.name} to {next_process.name}")
                    print("Ending simulation due to undefined transition.\n")
                    self.current_process = None

        print(f"Total surgery time: {self.total_time/60:.2f} min")
        print(f"Total transition time: {self.transition_time:.2f} sec\n")


    def get_simulation_history(self):
        print(f"Process history of simulation:")
        for process, time in self.history:
            print(f"  {process:<37}: {time/60:.2f} min")
        return self.history


    # Simulate a simple surgery
    #def run(self, current_process: str):
        #self.current_process = current.process
        #while self.current_process:
            #print(f"Current process: {self.current_process.name} (Duration: {self.current_process.duration})")
            #current_process = current_process.get_next_process(self.global_vars)
        #print("Surgery completed.")