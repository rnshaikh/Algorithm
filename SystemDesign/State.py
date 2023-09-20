"""
Context: Defines an interface for clients to interact. It maintains references to concrete state objects which may be used to define the current state of objects.
State: Defines interface for declaring what each concrete state should do.
ConcreteState: Provides the implementation for methods defined in State.
Example of State Design Pattern In the below example, we have implemented a mobile state scenario. With respect to alerts, a mobile can be in different states. For example, vibration and silence. Based on this alert state, the behavior of the mobile changes when an alert is to be done. 

"""
class State:
    
    def alert(self):
        pass
    

class Voice(State):
    
    def alert(self):
        print("Voice ......")
        

class Vibration(State):
    
    def alert(self):
        print("Vibration........")
        
        
class AlertContext:
    
    def __init__(self):
        self.state = Voice()
    
    def set_state(self, state):
        self.state = state
    
    def alert(self):
        self.state.alert()
        

obj1 = AlertContext()
obj2 = AlertContext()

obj1.alert()
obj2.alert()

obj1.set_state(Vibration())
obj1.alert()

obj2.alert()











