class clock:

    def __init__(self, jam, menit, detik):
        self.jam = jam 
        self.menit = menit
        self.detik = detik

    def getjam (self):
        return self.jam

    def getmenit (self):
        return self.menit

    def getdetik (self):
        return self.detik

    def tambahjam (self, penambahanjam):
        self.jam += penambahanjam

    def tambahmnt (self,penambahanmnt):
        self.menit += penambahanmnt

    def tambahdtk (self,penambahandtk):
        self.detik += penambahandtk

jamtest = clock(1, 1, 1)

jamtest.tambahjam(2)
jamtest.tambahmnt(2)
jamtest.tambahdtk(5)

if 0 <= jamtest.jam <= 24 and 0 <= jamtest.menit <= 59 and 0 <= jamtest.detik <= 59:
    print(jamtest.getjam(), ":", jamtest.getmenit(), ":", jamtest.getdetik())
else:
    print("error")