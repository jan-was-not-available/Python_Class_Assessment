class Robot:
    def __init__(self, name, color):
        # initialize properties code here
        self.battery = int(100)
        self.durability = (105)
        self.productivity = (14)
        self.work = int()
        pass    
    
    def charge(self, amount):
        robot.battery = robot.battery +- int(input)
        return self.charge 
    
    def work(self, hours):
        hours = int(hours)
        self.battery -= hours * 10
        self.durability -= hours * 5
        self.productivity += hours * 8
        return f"{self.name} works for {hours} hours."
    
    def repair(self, durability):
        self.durability = self.durability + int(input)
        return self.durability