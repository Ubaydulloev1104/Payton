class aktyor:
    def __init__(self,fio,age,a_navik,films,premi):
        self.fio =fio
        self.age=age
        self.a_navik=a_navik
        self.films=films
        self.premi=premi
class film():
    def __init__(self,nazv,god,rejisyor,janr,ros,doh):
        self.nazv=nazv
        self.god=god
        self.rejisyor=rejisyor
        self.janr=janr
        self.ros=ros
        self.doh=doh
class comiksy:
    def __init__(self,nazv,god,proiz,pisatel,hudoj):
        self.nazv=nazv
        self.god=god
        self.proiz=proiz
        self.pisatel=pisatel
        self.hudoj=hudoj
aktyor2 = aktyor("Chris Evansm,","34,","10 years,","Avengers,","Oskar.")
print(aktyor2.fio,aktyor2.age,aktyor2.a_navik,aktyor2.films,aktyor2.premi)

films=film("Мистетили,","2012,","Джон Уидон,","фантастика,","120 млн","1.5 млрд.")
print(films.nazv,films.god,films.rejisyor,films.janr,films.ros,films.doh)
com=comiksy("Человек-Паук,","2018,","Марвел,","Стэн Ли,","Л.Дикаприо.")
print(com.nazv,com.god,com.proiz,com.pisatel,com.hudoj)
