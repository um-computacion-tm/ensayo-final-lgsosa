from dispositivo import Dispositivo

class Database():
    def __init__(self, template : dict):
        self.database = [] #listadata(vacia)
        lista = template.get('dispositivos')
        for datos in lista:
            self.database.append(Dispositivo(diccionario=datos))

    def delete_by_id(self, id):
        for i in range(len(self.database)): #lee la lista de la database
            if self.database[i].id == id:
                self.database.pop(i)    
                break

    def add_dispositivo(self, dispositivo: Dispositivo = None, diccionario=None):
        if dispositivo is not None:
            self.database.append(dispositivo)
        if diccionario is not None:
            self.database.append(Dispositivo(diccionario=diccionario))

