from object_classes import Object, Surgeon, Nurse, Patient, SurgicalRobot, SurgicalTool, SceneManager

head_surgeon = Surgeon("Dr. A")
head_surgeon.tiredness(0.2)
assisting_surgeon = Surgeon("Dr. B")
assisting_surgeon.tiredness(0.3)

scrub_nurse = Nurse("Nurse A")
circulating_nurse = Nurse("Nurse B")

patient1 = Patient("Patient A")

robot1 = SurgicalRobot("Robot A", "Model X")


scalpel = SurgicalTool("Scalpel", "opening")
light = SurgicalTool("Overhead Light", "Light")
drill = SurgicalTool("Drill", "opening")

scene_description = SceneManager()