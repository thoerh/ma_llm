from environment import Process
from environment import GlobalVariables
from environment import SurgicalSimulation

cleaning = Process("Cleaning", 10)
incision = Process("Incision", 15)
suturing = Process("Suturing", 20)
recovery = Process("Recovery", 30)

# Define transitions
cleaning.add_transition(incision, 0.9)
cleaning.add_transition(cleaning, 0.1)  # 10% chance to repeat cleaning

incision.add_transition(suturing, 0.8)
incision.add_transition(cleaning, 0.2)  # 20% chance to go back to cleaning

suturing.add_transition(recovery, 1.0)  # Always go to recovery after suturing

# Simulate a simple surgery
current_process = cleaning
while current_process:
    print(f"Current process: {current_process.name} (Duration: {current_process.duration})")
    current_process = current_process.get_next_process()

print("Surgery completed.")