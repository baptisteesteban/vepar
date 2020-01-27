class VeparFile:
    def __init__(self, frame_period=0, ls_flags=[]):
        self.frame_period = frame_period
        self.ls_flags = ls_flags
        
    @classmethod
    def parse_file(self, filename):
        new = VeparFile()
        
        f = open(filename, "r")
        new.frame_period = int(f.readline())
        flag = f.readline()
        while len(flag) > 0:
            new.ls_flags.append(flag[:-1])
            flag = f.readline()
        
        f.close()
        return new