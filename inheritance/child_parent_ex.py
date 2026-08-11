class Cloths:
    def __init__(self):
        self.__cname="cotton cloths"

    def get_cname(self):
        return self.__cname
    def set_cname(self,cname):
        self.__cname=cname      
         
class Shirt(Cloths):
    def print_cloth_detail(self):
        print(self.get_cname())
      #print(self.__cname) here we will get error shirtclass does not have attribute shirt __cname


obj = Shirt()
obj.print_cloth_detail()      
obj.set_cname("silk cloths")
obj.print_cloth_detail()