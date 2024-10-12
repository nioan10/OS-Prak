import uuid
from Space import Space

class Process():
    def __init__(self, size):
        self.id = uuid.uuid4()
        self.size = size     # в байта или в страницах   
        self.status = 0      #0-idle 1-running 2-wait
        self.countSpaces = 0
        self.Spaces = []
    
    def add_space(self, space: Space):
        self.Spaces.append(space)
        self.countSpaces += 1
    
    def clear_space(self):
        self.Spaces.clear()
        self.countSpaces = 0
    
    
