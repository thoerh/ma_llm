from environment import Process
from environment import GlobalVariables
from environment import SurgicalSimulation

from surgery_instances import initialize, cleaning, anesthesia, error, incision, knee_joint_preparation, bone_resurfacing, insertion_prosthetic, balancing_ligaments, insertion_spacer, closing_incision, post_operative_care, end
from surgery_instances import var_knee_surgery
from surgery_instances import basic_simulation






starting_process = initialize
basic_simulation.run(starting_process)