from environment import Process
from environment import GlobalVariables
from environment import SurgicalSimulation

from surgery_instances import initialize, cleaning, anesthesia, error_redo, incision, knee_joint_preparation, bone_resurfacing, insertion_prosthetic, balancing_ligaments, insertion_spacer, closing_incision, post_operative_care, end
from surgery_instances import var_knee_surgery




# Simulate a simple surgery
current_process = initialize
while current_process:
    print(f"Current process: {current_process.name} (Duration: {current_process.duration})")
    current_process = current_process.get_next_process(var_knee_surgery)

print("Surgery completed.")