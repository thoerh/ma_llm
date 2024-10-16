# here are the classes defined which should differ forvarying surgeries like the:
#       Process instances
#       Probabilities for surgical simulation  
#       Scene describing Variables initialized  
# 
#       Scene graph instances    


from environment_classes import Process, GlobalVariables, SurgicalSimulation

from object_instances import head_surgeon, assisting_surgeon, scrub_nurse, circulating_nurse, patient1, robot1, scalpel, drill, disinfectant, anesthetics, prosthesis, thread


var_knee_surgery = GlobalVariables(0.8, 0.7, 0.7)



initialize = Process("Initialize", 5)
cleaning = Process("Cleaning", 10)
anesthesia = Process("Anesthesia", 15)
incision = Process("Incision", 20)
insertion_prosthetic = Process("Insertion of Prosthetic Components", 35)
closing_incision = Process("Closing of Incision", 20)
end = Process("End", 5)
error = Process("Error", 15)



# Define transitions
initialize.add_transition(cleaning, 0.9)
initialize.add_redo_transition(0.1)

cleaning.add_transition(anesthesia, 0.8)
cleaning.add_redo_transition(0.15)
cleaning.add_alt_transition(error, 0.05)

anesthesia.add_transition(incision, 0.9)
anesthesia.add_redo_transition(0.1)

incision.add_transition(insertion_prosthetic, 0.7)
incision.add_redo_transition(0.3)  

insertion_prosthetic.add_transition(closing_incision, 0.76)
insertion_prosthetic.add_redo_transition(0.12)
insertion_prosthetic.add_alt_transition(error, 0.12)

closing_incision.add_transition(end, 0.8)
closing_incision.add_redo_transition(0.1)
closing_incision.add_alt_transition(error, 0.1)



#Description of processes and of objects during the specific processes       
initialize.add_object_attribute(head_surgeon, {"position": (1, 2)})
initialize.add_object_attribute(assisting_surgeon, {"position": (2, 2), "tiredness_level": 0.0})
initialize.add_object_attribute(scrub_nurse, {"position": (3, 2), "inventory": [disinfectant]})
initialize.add_object_attribute(disinfectant, {"position": (3,2), "in_use": False})
initialize.add_object_attribute(patient1, {"position": (1.5, 1), "knee_position": (0.5, 1)})
initialize.add_object_attribute(robot1, {"position": (3, 1), "current_tool": drill})
initialize.add_object_attribute(circulating_nurse, {"position": (2,3), "inventory": []})

cleaning.add_object_attribute(disinfectant, {"position": (0.5, 1), "in_use": True})
cleaning.add_object_attribute(scrub_nurse, {"position": (0.5, 1), "inventory": [disinfectant]})
cleaning.add_object_attribute(circulating_nurse, {"position":(2, 1), "inventory": [anesthetics]})

anesthesia.add_object_attribute(circulating_nurse, {"position":(2, 1), "inventory": [scalpel, anesthetics]})
anesthesia.add_object_attribute(scrub_nurse, {"position":(2, 0.5), "inventory": [anesthetics]})

incision.add_object_attribute(scrub_nurse, {"position":(2, 0.5), "inventory": []})
incision.add_object_attribute(head_surgeon, {"position": (0.5, 1), "tiredness_level": 0.3, "current_tool": scalpel})
incision.add_object_attribute(circulating_nurse, {"position": (0.5, 1.5), "inventory": [prosthesis]})
incision.add_object_attribute(assisting_surgeon, {"position": (0, 1), "tiredness_level": 0.1, "current_tool": None})

insertion_prosthetic.add_object_attribute(head_surgeon, {"position": (0.5, 1), "tiredness_level": 0.4, "current_tool": prosthesis})
insertion_prosthetic.add_object_attribute(assisting_surgeon, {"position": (0, 1), "tiredness_level": 0.2, "current_tool": prosthesis})
insertion_prosthetic.add_object_attribute(circulating_nurse, {"position": (0.5, 1.5), "inventory": []})

closing_incision.add_object_attribute(head_surgeon, {"position": (0.5, 1), "tiredness_level": 0.5, "current_tool": thread})





#initialize a simulation
basic_simulation = SurgicalSimulation(var_knee_surgery)
#basic_simulation.set_start_process(initialize)