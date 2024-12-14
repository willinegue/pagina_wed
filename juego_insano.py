import speech_recognition as sr
import random
import time

def speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Habla ahora...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            print("Procesando tu respuesta...")
            return recognizer.recognize_google(audio, language="fr-FR")
        except sr.UnknownValueError:
            print("No se entendió lo que dijiste.")
            return None
        except sr.WaitTimeoutError:
            print("No detecté ninguna respuesta.")
            return None
        except Exception as e:
            print(f"Error inesperado: {e}")
            return None

def play_game():
    niveles = {
        "facil": ["agenda", "ami", "souris"],
        "intermedio": ["ordinateur", "algorithme", "développeur"],
        "dificil": ["réseau neuronal", "apprentissage automatique", "intelligence artificielle"]
    }

    print("Bienvenido al juego de pronunciación en francés!")
    nivel = ""
    while nivel not in niveles:
        nivel = input("Selecciona un nivel (facil, intermedio, dificil): ").lower()

    palabras = niveles[nivel]
    puntuacion = 0

    print(f"Has seleccionado el nivel {nivel}. Pronuncia correctamente las palabras para ganar puntos. Tienes 3 intentos por palabra y 5 segundos por intento.\n")

    for palabra in palabras:
        print(f"Nueva palabra: {palabra}")
        intentos = 3
        reconocida = False

        while intentos > 0 and not reconocida:
            print(f"Tienes {intentos} intento(s) restante(s).")
            respuesta = speech()

            if respuesta:
                print(f"Tu respuesta: {respuesta}")
                if respuesta.lower() == palabra:
                    print("\u2714 Correcto! Has ganado un punto.\n")
                    puntuacion += 1
                    reconocida = True
                else:
                    print("\u274C Incorrecto. Intenta de nuevo.\n")
            else:
                print("Por favor, intenta de nuevo.\n")

            intentos -= 1

        if not reconocida:
            print(f"No lograste pronunciar la palabra '{palabra}'. Pasemos a la siguiente palabra.\n")

        time.sleep(1)

    print(f"\nJuego terminado! Tu puntuación final es: {puntuacion}/{len(palabras)}")

if __name__ == "__main__":
    play_game()
