class Dispositivo():
    def __init__(self, id = 0, nombre = '', marca = '', tipo = '', diccionario = None):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.marca = marca

        if diccionario is not None:
            if 'id' in diccionario:
                self.id = diccionario.get('id')
            if 'nombre' in diccionario:
                self.nombre = diccionario.get('nombre')
            if 'tipo' in diccionario:
                self.tipo = diccionario.get('tipo')
            if 'marca' in diccionario:
                self.marca = diccionario.get('marca')
