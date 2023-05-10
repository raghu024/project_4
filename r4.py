class rectangle:
    def __init__(self,leng,bred):
        self.leng=leng
        self.bred=bred
        self.area=self.leng*self.bred
s=rectangle(100,100)
print(s.__dict__)
