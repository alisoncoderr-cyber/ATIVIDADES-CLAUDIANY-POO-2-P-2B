class Celular:
    marca = "..."
    modelo = "..."

    def definir_marca(self, nova_marca):
        self.marca = nova_marca

    def definir_modelo(self, novo_modelo):
        self.modelo = novo_modelo


meu_celular = Celular()
meu_celular.definir_marca("Samsung")
meu_celular.definir_modelo("Galaxy S23")

print("Marca:", meu_celular.marca)
print("Modelo:", meu_celular.modelo)


