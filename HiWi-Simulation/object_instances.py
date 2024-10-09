from object_classes import Person, Surgeon, Nurse, Patient, SurgicalRobot, SurgicalTool, SceneManager

head_surgeon = Surgeon("Dr. A")
assisting_surgeon = Surgeon("Dr. B")
scrub_nurse = Nurse("Nurse A")
circulating_nurse = Nurse("Nurse B")
current_patient = Patient("Patient A")
roboter = SurgicalRobot("Robo, Model X")
scalpel = SurgicalTool("Scalpel", "opening")
light = SurgicalTool("Overhead Light", "Light")
driller = SurgicalTool("Driller", "opening")
scene_description = SceneManager()