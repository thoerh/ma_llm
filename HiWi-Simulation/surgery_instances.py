# here are the classes defined which should differ forvarying surgeries like the:
#       Process instances
#       Probabilities for surgical simulation  
#       Scene describing Variables initialized  
# 
#       Scene graph instances    


from environment import Process
from environment import GlobalVariables

initialize = Process("Initialize")
cleaning = Process("Cleaning")
anesthesia = Process("Anesthesia")
error_redo = Process("Error/Redo")
incision = Process("Incision")
knee_joint_preparation = Process("Knee Joint Preparation")
bone_resurfacing = Process("Bone Resurfacing")
insertion_prosthetic = Process("Insertion of Prosthetic Components")
balancing_ligaments = Process("Balancing of Ligaments")
insertion_spacer = Process("Insertion of Spacer")
closing_incision = Process("Closing of Incision")
post_operative_care = Process("Post-operative Care")
error_redo = Process("Error/Redo")
end = Process("End")

