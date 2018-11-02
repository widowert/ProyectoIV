import os

class Cita:
    def __init__(self,date,hour,username):
        self.date=date
        self.hour=hour
        self.username=username
class Calendario:
    #Clase del calendario, que será entorno a lo que gire todo
    #posteriormente
    def __init__(self):
        self.dOcuped=[]

    def setCalendario(self,month,year):
        cl=calendar.HTMLCalendar()
        calendario=cl.formatmonth(year,month)
        with open("./templates/calendario.html","w") as html:
            html.write(calendario)
            html.close()

    def generaCalendarioHoyHTML(self):
        x=datetime.datetime.now()
        cl=calendar.HTMLCalendar()
        calendario=cl.formatmonth(x.year,x.month)
        with open("./templates/calendario.html","w") as html:
            html.write(calendario)
            html.close()

    def aniadirCita(self,cita):
        self.dOcuped.append(str(cita.day)+"/"+str(cita.month)+"/"+str(cita.year))
        print(self.dOcuped)
        print(str(cita.day)+"/"+str(cita.month)+"/"+str(cita.year))

    def getOcuped(self):
        return self.dOcuped
