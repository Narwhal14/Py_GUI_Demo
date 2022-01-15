class Events:
    #the various event settings


    def __init_subclass__(self, startH, startM, endH, endM,pump,light):
        self.startH = startH
        self.startM = startM
        self.endH = endH
        self.endM = endM
        self.pump = pump
        self.light = light