import  time
class Bilgisayar():
    def __init__(self,bilgisayar_durum="kapalı",bilgisayar_volume=0,bilgisayar_modelleri=["lenova"]):
        self.bilgisayar_durum=bilgisayar_durum
        self.bilgisayar_volume=bilgisayar_volume
        self.bilgisayar_modelleri=bilgisayar_modelleri
    def bilgisayarı_aç(self):
        if(self.bilgisayar_durum=="açık"):
            print("bilgisayar zaten açık")
        else:
            print("bilgisayar açılıyor")
            self.bilgisayar_durum="açık"
    def bilgisayarı_kapat(self):
        if(self.bilgisayar_durum=="kapalı"):
            print("pc zaten kapalı")
        else:
            print("pc kapanıyor")
            self.bilgisayar_durum="kapalı"
    def bilgisayar_ses(self):
        while True:
            cevap=input("pc'nin sesini açmak için '>'\n  pc'nin sesini kapamak için '<'\n çıkış için: çıkış\n ")
            if(cevap==">"):
                if(self.bilgisayar_volume!=31):

                    self.bilgisayar_volume+=1
                    print("ses arttı",self.bilgisayar_volume)
            elif(cevap=="<"):
                if(self.bilgisayar_volume!=0):

                   self.bilgisayar_volume-=1
                   print("ses azaldı",self.bilgisayar_volume)
            else:
                print("ses güncellendi",self.bilgisayar_volume)
                break

    def bilgisayar_modeller(self,bilgisayar_modellerin):
        print("bilgisayar modeli ekleniyor")
        time.sleep(2)
        self.bilgisayar_modelleri.append(bilgisayar_modellerin)
        print("bilgisayar modelleri eklendi")

    def __str__(self):
        return("bilgisayar_durum {}\nbilgisayar_volume : {} \nbilgisayar_modelleri : {}").format(self.bilgisayar_durum,self.bilgisayar_volume,self.bilgisayar_modelleri)
bilgisayar=Bilgisayar()
print("""
1.pc aç
2.pc kapa
3.pc ses ayarları
4.bilgisayar modelleri
5.pc model listesi
""")
while True:
    işlem=input("lütfen yapmak istedigin işlemi seçiniz")
    if(işlem=="1"):
        bilgisayar.bilgisayarı_aç()
    elif (işlem == "2"):
         bilgisayar.bilgisayarı_kapat()
    elif(işlem=="3"):
        bilgisayar.bilgisayar_ses()

    elif (işlem == "4"):
        bilgisayar_modelleri = input("pc modelleri isimlerini ',' ile ayırarak girin:")

        bilgisayar_modelleri = bilgisayar_modelleri.split(",")

        for eklenecekler in bilgisayar_modelleri:
            bilgisayar.bilgisayar_modeller(eklenecekler)
    elif(işlem=="5"):
        print(bilgisayar)
    else:
        print("gecersiz işlem")








