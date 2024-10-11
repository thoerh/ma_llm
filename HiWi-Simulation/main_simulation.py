from environment_classes import Process
from environment_classes import GlobalVariables
from environment_classes import SurgicalSimulation

from environment_instances import initialize, cleaning, anesthesia, error, incision, insertion_prosthetic, closing_incision, end
from environment_instances import var_knee_surgery
from environment_instances import basic_simulation






starting_process = initialize
basic_simulation.run(starting_process)