class utama():
    def __init__ (self, nama, NIM) :
        self.nama = nama
        self.NIM = NIM

    def data (self) :
        print(f"nama : {self.nama}")
        print(f"NIM  : {self.NIM}")

class mahasiswa (utama):
    pass

mhs1 = mahasiswa ("Vindy", 20210801309)
mhs1.data()
print("-----------------------------------")
mhs2 = utama ("Vindy", 20210801309)
mhs2.data()