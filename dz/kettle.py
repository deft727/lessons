
#KS_OK = 'ok'
#KS_OVERFLOW = 'overflow'


class Kettle :
    def __init__(self, volume, power, color) :
        self.LS_OPEN = True
        self.LS_CLOSE = False
        self.vol = volume
        self.pwr = power
        self.clr = color
        self.onOff = False
        self.lidStatus = self.LS_CLOSE
        self.currentVolume = 0
        #self.kettleStatus = KS_OK
        self.waterTemp = 20
    
    def on(self) :
        
        if self.isEmpty() == True or self.isOverflow() == True :
            print ("Can't on the kettle")
            return
        if self.isLidOpen() == False :
            self.onOff = True
        else :
            print ("The lid isn't closed")

    def off(self) :
        self.onOff = False

    def isOnOff(self) :
        return self.onOff
    
    def getColor(self) :
        return self.clr
    
    # def setColor(self, color) :
    #     self.clr = color

    def openLid(self) :
        self.lidStatus = self.LS_OPEN

    def closeLid(self) :
        self.lidStatus = self.LS_CLOSE

    def isEmpty(self) :
        if self.currentVolume > 0 and self.currentVolume <= self.vol:
            return False # не пустой
        else :
            return True # пустой

    def isFull(self) :
        if self.currentVolume >= self.vol:
            return True 
        else :
            return False 

    def isOverflow(self) :
        if self.currentVolume > self.vol:
            return True 
        else :
            return False 

    def isLidOpen(self) :
        if self.lidStatus == self.LS_OPEN :
            return True
        else :
            return False

    def addWater(self, waterVolume) :
        
        if self.isLidOpen() == False :
            print("Can't add water")
            return
            #self.openLid()
        if self.isFull() == True :
            print("The kettle is full")
            return
        self.currentVolume += waterVolume

    def boilKettle(self, endTemp, step) :
        
        for i in range(self.waterTemp, endTemp, step) :
            print("Water temperature is:", i)

