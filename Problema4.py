import random

class RecomendadorPeliculas:
    def __init__(self):
        # Diccionario de películas organizadas por género
        self.peliculas = {
            "acción": ["Mad Max: Fury Road", "John Wick", "Die Hard"],
            "comedia": ["Superbad", "The Hangover", "Step Brothers"],
            "drama": ["The Shawshank Redemption", "Forrest Gump", "The Godfather"],
            "ciencia ficción": ["Inception", "The Matrix", "Interstellar"],
            "terror": ["Get Out", "A Nightmare on Elm Street", "The Conjuring"]
        }

    def recomendar(self, genero):
        # Verificar si el género está en el diccionario
        if genero in self.peliculas:
            # Seleccionar una película aleatoria del género indicado
            recomendacion = random.choice(self.peliculas[genero])
            return f"Te recomendamos ver: {recomendacion}"
        else:
            return "Lo siento, no tenemos recomendaciones para ese género."

# Crear el agente de recomendación
recomendador = RecomendadorPeliculas()

# Pedir al usuario su género favorito
genero_usuario = input("¿Cuál es tu género de película favorito? (acción, comedia, drama, ciencia ficción, terror): ").lower()
resultado = recomendador.recomendar(genero_usuario)
print(resultado)
