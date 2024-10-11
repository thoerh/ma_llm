# here are the classes defined which should differ forvarying surgeries like the:
#       Process instances
#       Probabilities for surgical simulation  
#       Scene describing Variables initialized  
# 
#       Scene graph instances    


from environment_classes import Process, GlobalVariables, SurgicalSimulation

from object_instances import head_surgeon, assisting_surgeon, scrub_nurse, circulating_nurse, patient1, robot1, scalpel, light, drill


var_knee_surgery = GlobalVariables(0.2, 0.7, 0.7)



initialize = Process("Initialize", 5)
cleaning = Process("Cleaning", 10)
anesthesia = Process("Anesthesia", 15)
error = Process("Error", 5)
incision = Process("Incision", 20)
knee_joint_preparation = Process("Knee Joint Preparation", 30)
bone_resurfacing = Process("Bone Resurfacing", 25)
insertion_prosthetic = Process("Insertion of Prosthetic Components", 35)
balancing_ligaments = Process("Balancing of Ligaments", 15)
insertion_spacer = Process("Insertion of Spacer", 10)
closing_incision = Process("Closing of Incision", 20)
post_operative_care = Process("Post-operative Care", 40)
end = Process("End", 5)



# Define transitions
initialize.add_transition(cleaning, 0.9)
initialize.add_redo_transition(0.1)

cleaning.add_transition(anesthesia, 0.8)
cleaning.add_redo_transition(0.15) 
cleaning.add_alt_transition(error, 0.05)

anesthesia.add_transition(incision, 0.9)
anesthesia.add_redo_transition(0.1)

incision.add_transition(knee_joint_preparation, 0.5)
incision.add_redo_transition(0.5)  

knee_joint_preparation.add_transition(insertion_prosthetic, 1.0)

insertion_prosthetic.add_transition(end, 0.6)
insertion_prosthetic.add_redo_transition(0.2)
insertion_prosthetic.add_alt_transition(knee_joint_preparation, 0.2)



#Description of processes and of objects during the specific processes       
initialize.add_object_attribute(head_surgeon, {"position": (1, 2), "tiredness_level": 0.0})
initialize.add_object_attribute(assisting_surgeon, {"position": (2, 2), "tiredness_level": 0.0})
initialize.add_object_attribute(scrub_nurse, {"position": (3, 2), "inventory": []})
initialize.add_object_attribute(patient1, {"position": (0, 0), "knee_position": (0, 0)})
initialize.add_object_attribute(robot1, {"position": (1, 1), "current_tool": None})








#initialize a simulation
basic_simulation = SurgicalSimulation(var_knee_surgery)
#basic_simulation.set_start_process(initialize)