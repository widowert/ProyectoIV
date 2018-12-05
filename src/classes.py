import os,json
from flask import jsonify

class Citas:
    #Clase cita con los metodos necesarios para la extraccion
    #de citas especificas desde json
    def __init__(self):
        #Para leer los archivos solo una vez y comprobar antes
        #de su uso que se leen correctamente
        self.testing=False
        try:
            if os.path.exists('data/freeDates.json'):
                with open('data/freeDates.json') as file:
                    self.freeDatesFile=json.load(file)
            else:
                raise IOError("Cant find freeDates.json")
            if os.path.exists('data/occupiedDates.json'):
                with open('data/occupiedDates.json') as file:
                    self.occupiedDatesFile=json.load(file)
            else:
                raise IOError("Cant find occupiedDates.json")
        except IOError as error:
                 print("Error leyendo archivos json".format(error))

    def getFreeDates(self,dia,mes,anio=18):
        freeDates=[]
        searchDate=str(dia)+"/"+str(mes)+"/"+str(anio)
        for date in self.freeDatesFile['dates']:
            if date['date'] == searchDate:
                freeDates.append(date)
        if freeDates == []:
            if self.testing:
                return "ERROR"
            else:
                return jsonify({'Error':"ERROR",
                'Message':"No se han encontrado citas libres para la fecha "+ searchDate})
        else:
            if self.testing:
                return "FOUND"
            else:
                return jsonify(freeDates)

    def getAllFreeDates(self):
        freeDates=[]
        for date in self.freeDatesFile['dates']:
            freeDates.append(date)
        if freeDates == []:
            if self.testing:
                return "ERROR"
            else:
                return jsonify({'Error':"Dates not found",
                'Message':"No se han encontrado citas libres"})
        else:
            if self.testing:
                return "FOUND"
            else:
                return jsonify(freeDates)
                #return jsonify(freeDates[1])

    def getMyDates(self,username):
        myDates=[]
        for date in self.occupiedDatesFile:
            if date['username'] == str(username):
                myDates.append(date)
        if myDates == []:
            if self.testing:
                return "ERROR"
            else:
                return jsonify({'Error':"Dates not found",
                'Message':"No se han encontrado citas para el usuario"+str(username)})
        else:
            if self.testing:
                return "FOUND"
            else:
                return jsonify(myDates)

    def getAllOccupiedDates(self):
        occupiedDates=[]
        for date in self.occupiedDatesFile:
            occupiedDates.append(date)
        if occupiedDates == []:
            if self.testing:
                return "ERROR"
            else:
                return jsonify({'Error':"Dates not found",
                'Message':"No se han encontrado citas registradas"})
        else:
            if self.testing:
                return "FOUND"
            else:
                return jsonify(occupiedDates)

    def setTestingClass(self,value=False):
        self.testing=value

    def deleteFreeDate(self,theDate,theHour):
        count=0
        result=False
        if os.path.exists('data/freeDates.json'):
            with open('data/freeDates.json',"r+") as file:

                data=json.load(file)
                for date in data['dates']:
                    if date['date'] == theDate and date['hour'] == theHour:
                        data['dates'].pop(count)
                        result=True
                    count+=1
                file.seek(0)
                json.dump(data,file)
                file.truncate()
        else:
            raise IOError("Cant find freeDates.json")
        if result:
            return jsonify({"return":"Deleted succesfully"})
        else:
            return jsonify({"return":"Cant delete, didnt find it"})

    def addFreeDate(self,theDate,theHour):
        count=0
        right=0
        if os.path.exists('data/freeDates.json'):
            with open('data/freeDates.json',"r+") as file:

                data=json.load(file)
                for date in data['dates']:
                    if date['date'] == theDate:
                        if date['hour'] == theHour:
                            return jsonify({"ERROR":"Ya existe esta cita"})
                        right=count
                    count+=1
                tmp={"date":theDate,
                    "hour":theHour}
                data['dates'].insert(right+1,tmp)
                file.seek(0)
                json.dump(data,file)
                #file.truncate()
        else:
            raise IOError("Cant find freeDates.json")
        return jsonify({"result":"Cita aniadida correctamente"})

    def deleteOccupiedDate(self,theDate,theHour):
        count=0
        result=False
        if os.path.exists('data/occupiedDates.json'):
            with open('data/occupiedDates.json',"r+") as file:

                data=json.load(file)
                for date in data:
                    if date['date'] == theDate and date['hour'] == theHour:
                        data.pop(count)
                        result=True
                    count+=1
                file.seek(0)
                json.dump(data,file)
                file.truncate()
        else:
            raise IOError("Cant find freeDates.json")
        if result:
            return jsonify({"return":"Deleted succesfully"})
        else:
            return jsonify({"return":"Cant delete, didnt find it"})

    def addOccupiedDate(self,theDate,theHour,theUser):
        count=0
        right=0
        if os.path.exists('data/occupiedDates.json'):
            with open('data/occupiedDates.json',"r+") as file:
                data=json.load(file)
                for date in data:
                    if date['date'] == theDate:
                        if date['hour'] == theHour:
                            return jsonify({"ERROR":"Ya existe esta cita"})
                        right=count
                    count+=1
                tmp={"username":theUser,
                    "date":theDate,
                    "hour":theHour}
                data.insert(right,tmp)
                file.seek(0)
                json.dump(data,file)
                #file.truncate()
        else:
            raise IOError("Cant find freeDates.json")
        return jsonify({"result":"Cita aniadida correctamente"})
#class Usuario:
    #Clase para la identificacion y posterior gestion de citas
