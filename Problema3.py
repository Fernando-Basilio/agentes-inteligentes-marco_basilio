class SistemaExperto:
    def diagnosticar(self, sintomas):
        if "fiebre" in sintomas and "tos" in sintomas:
            return "Posible gripe."
        elif "dolor de cabeza" in sintomas and "nauseas" in sintomas:
            return "Posible migraña."
        elif "dolor de garganta" in sintomas:
            return "Posible faringitis."
        else:
            return "Síntomas no reconocidos. Consulte a un médico."

# Solicitar síntomas al usuario
sintomas_usuario = input("Ingrese sus síntomas separados por comas: ").split(", ")
sistema = SistemaExperto()
diagnostico = sistema.diagnosticar(sintomas_usuario)
print(diagnostico)
