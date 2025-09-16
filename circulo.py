class Circulo:
    def __init__ (self, cx,cy,radio):
        if cx is None and cy is None and radio is None:
            self.cx = self.cy = 0
            self.radio = 1.0
        else:
            self.cx = cx
            self.cy = cy
            self.radio = radio
    
    def getCx(self):
        return self.cx
    def getCy(self):
        return self.cy
    def getradio(self):
        return self.radio
    def setCx(self, cx = None):
        if cx is None or cx is not isinstance(cx, int):
            cx=0
        else:
            self.cx = cx
    def setCy(self, cy= None):
        if cy is None or cy is not isinstance(cy, int):
            cy=0
        else:
            self.cy = cy
    
    def setRadio(self, radio = None):
        if radio is None or radio is not isinstance(radio, int):
            radio=1.0
        else:
            self.radio = radio
    def toString(self):
        return f"Circulo: Centro: ({self.cx},{self.cy}) Radio: {self.radio}"


c1=Circulo(2,2,2.0)
print(c1.toString())