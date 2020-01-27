class VeparFile:
    def __init__(self, frame_period=None, ls_flags=[]):
        self.frame_period = frame_period
        self.ls_flags = ls_flags
        
    @classmethod
    def parse_file(self, filename):
        new = VeparFile()
        
        f = open(filename, "r")
        flag = f.readline()
        if flag not in ["TOP_FIELD_FIRST\n", "PROGRESSIVE_FRAME\n", "REPEAT_FIRST_FIELD\n"]:
            new.frame_period = int(flag)
            flag = f.readline()
        while len(flag) > 0:
            new.ls_flags.append(flag[:-1])
            flag = f.readline()
        
        f.close()
        return new
    
    def __str__(self):
        return "{\n\t\"frame_period\": " + str(self.frame_period) + ",\n\t\"frame_flags\":" + str(self.ls_flags) + ",\n\t\"nb_frame\": " + str(len(self.ls_flags)) + "\n}"