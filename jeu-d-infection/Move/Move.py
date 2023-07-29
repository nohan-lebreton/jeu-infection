# Représente un coup

class Move :
    def __init__(self, posI_x, posI_y, posA_x, posA_y, typeName):
        self.posI_x = posI_x
        self.posI_y = posI_y
        self.posA_x = posA_x
        self.posA_y = posA_y
        self.typeName = typeName
    
    def afficheAttributs(self):
        return self.posI_x ,self.posI_y ,self.posA_x ,self.posA_y  , self.typeName
    
    def getType(self) :
        return self.typeName

    def getPosI_x(self) :
        return self.posI_x

    def getPosI_y(self) :
        return self.posI_y

    def getPosA_x(self) :
        return self.posA_x

    def getPosA_y(self) :
        return self.posA_y