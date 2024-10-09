from environment_classes import Process
from environment_classes import GlobalVariables
from environment_classes import SurgicalSimulation

from environment_instances import initialize, cleaning, anesthesia, error, incision, knee_joint_preparation, bone_resurfacing, insertion_prosthetic, balancing_ligaments, insertion_spacer, closing_incision, post_operative_care, end
from environment_instances import var_knee_surgery
from environment_instances import basic_simulation






starting_process = initialize
basic_simulation.run(starting_process)