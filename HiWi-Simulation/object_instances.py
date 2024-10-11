from object_classes import Object, Surgeon, Nurse, Patient, SurgicalRobot, SurgicalTool, SceneManager

head_surgeon = Surgeon("Headsurgeon A")
head_surgeon.tiredness(0.2)
assisting_surgeon = Surgeon("Assisting Surgeon B")

scrub_nurse = Nurse("Scrub Nurse A")
circulating_nurse = Nurse("Circulating Nurse B")

patient1 = Patient("Patient A")

robot1 = SurgicalRobot("Robot A", "Model X")


scalpel = SurgicalTool("Scalpel", "opening")
light = SurgicalTool("Overhead Light", "Light")
drill = SurgicalTool("Drill", "opening")
disinfectant = SurgicalTool("Disinfectant", "cleaning")
anesthetics = SurgicalTool("Anesthetics", "anesthesia")
prosthesis = SurgicalTool("Prosthesis", "implant")
thread = SurgicalTool("Surgical Thread", "closing")

scene_description = SceneManager()