class sapa:
    def hai(self):
        raise NotImplementedError("")

class nihon(sapa):
    def hai (self):
        print ('nyahallo~~~')

class indo(sapa):
    def hai (self):
        print ('halo')
        
def salam (sapa):
        sapa.hai()

a = nihon()
b = indo()

salam(a)
salam(b)