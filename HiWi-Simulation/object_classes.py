
class Object:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
        self.position = (0, 0) 
        self.tiredness_level = 0.0

    def move(self, new_position: tuple[float, float]):
        self.position = new_position
        return new_position

    def tiredness(self, level: float = None):
        if level is not None:
            self.tiredness_level = level

class Surgeon(Object):
    def __init__(self, name):
        super().__init__(name, "Surgeon")
        self.current_tool = None

    def pick_up_tool(self, tool):
        self.current_tool = tool

    def put_down_tool(self):
        self.current_tool = None

class Nurse(Object):
    def __init__(self, name):
        super().__init__(name, "Nurse")
        self.inventory = []

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def remove_from_inventory(self, item):
        if item in self.inventory:
            self.inventory.remove(item)

class Patient(Object):
    def __init__(self, name):
        super().__init__(name, "Patient")
        self.knee_position = (0, 0)

    def position_for_surgery(self, position: tuple[float, float], knee_position: tuple[float,float]):
        self.position = position
        self.knee_position = knee_position

class SurgicalRobot(Object):
    def __init__(self, name, model):
        super().__init__(name, "Robot")
        self.model = model
        self.current_tool = None

    def move(self, new_position):
        self.position = new_position

    def attach_tool(self, tool):
        self.current_tool = tool

    def detach_tool(self):
        self.current_tool = None

class SurgicalTool(Object):
    def __init__(self, name, tool_type):
        super().__init__(name, "Tool")
        self.tool_type = tool_type
        self.in_use = False

    def move(self, new_position):
        self.position = new_position

    def use(self):
        self.in_use = True

    def release(self):
        self.in_use = False

class SceneManager:
    def __init__(self):
        self.surgeons = []
        self.nurses = []
        self.patients = []
        self.robots = []
        self.tools = []

    def add_surgeon(self, surgeon):
        self.surgeons.append(surgeon)

    def add_nurse(self, nurse):
        self.nurses.append(nurse)

    def add_patient(self, patient):
        self.patients.append(patient)

    def add_robot(self, robot):
        self.robots.append(robot)

    def add_tool(self, tool):
        self.tools.append(tool)

    def get_scene_state(self):
        return {
            "surgeons": self.surgeons,
            "nurses": self.nurses,
            "patients": self.patients,
            "robots": self.robots,
            "tools": self.tools
        }