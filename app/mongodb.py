from pymongo import MongoClient

class MongoDB:
    def __init__(self):
        self.MONGO_URI = 'mongodb://localhost:27017/'
        self.DATABASE_NAME = 'infoCalculadora'
        self.COLLECTION_NAME_SUM = 'sum_operacion'
        self.COLLECTION_NAME_REST = 'rest_operacion'
        self.COLLECTION_NAME_MULTIPLI = 'multipli_operacion'
        self.COLLECTION_NAME_DIV = 'div_operacion'
        self.client = MongoClient(self.MONGO_URI)
        self.db = self.client[self.DATABASE_NAME]
        self.collection_sum = self.db[self.COLLECTION_NAME_SUM]
        self.collection_rest = self.db[self.COLLECTION_NAME_REST]
        self.collection_multipli = self.db[self.COLLECTION_NAME_MULTIPLI]
        self.collection_div = self.db[self.COLLECTION_NAME_DIV]

    def guardar_operacion(self, expresion, resultado, operacion):
        try:
            if operacion == '+':
                self.collection_sum.insert_one({'expresion': expresion, 'resultado': resultado})
                print("Operación de suma guardada en MongoDB.")
            elif operacion == '-':
                self.collection_rest.insert_one({'expresion': expresion, 'resultado': resultado})
                print("Operación de resta guardada en MongoDB.")
            elif operacion == '*':
                self.collection_multipli.insert_one({'expresion': expresion, 'resultado': resultado})
                print("Operación de multiplicación guardada en MongoDB.")
            elif operacion == '/':
                self.collection_div.insert_one({'expresion': expresion, 'resultado': resultado})
                print("Operación de división guardada en MongoDB.")
            else:
                print("Operación no reconocida. No se guardó en MongoDB.")
        except Exception as e:
            print("Error al guardar la operación en MongoDB:", str(e))

    def cerrar_conexion(self):
        self.client.close()




