class Libro():
    
    def __init__(self, titulo = "", paginas = 0, precio = 0.0,\
                  digital = False, tapa = "blanda", envio = "standar", id = 0):
        self.titulo = titulo
        self.paginas = paginas
        self.precio = precio
        self.digital = digital
        self.tapa = tapa
        self.envio = envio
        self.id = id