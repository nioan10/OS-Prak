from interface import implements, Interface
from process import Process

class IMemoryManager(Interface):
    def __init__(self, size, sizeOfSpace, compress): 
        pass
    def allocate_memory(self, process: Process):
        pass
    def release_memory(self, process: Process):
        pass
    def wakeup_process(self, process: Process):
        pass
    def get_status(self):
        pass
    

