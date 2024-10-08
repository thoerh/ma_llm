# here are the classes defined which should differ forvarying surgeries like the:
#       Process instances
#       Probabilities for surgical simulation  
#       Scene describing Variables initialized  
# 
#       Scene graph instances    


from environment import Process
from environment import GlobalVariables
from environment import SurgicalSimulation


var_knee_surgery = GlobalVariables(0.7, 0.7, 0.7)



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


basic_simulation = SurgicalSimulation(var_knee_surgery)
#basic_simulation.set_start_process(initialize)