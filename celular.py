class Celular:
 
    def definir_marca(self, nova_marca):
        self.marca = nova_marca

    def definir_modelo(self, novo_modelo):
        self.modelo = novo_modelo
        
celular = Celular()
celular.definir_marca("Samsung")
celular.definir_modelo("Galaxy S23")

print("Marca:", celular.marca)
print("Modelo:", celular.modelo)
