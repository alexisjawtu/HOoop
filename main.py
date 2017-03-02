import radar
import medio
import blanco
import generador
import datetime
import detector

def main():

    # Intervalo de tiempo en el que vamos a medir
    tiempo_inicial  = datetime.datetime(2016, 3, 5, 1)
    tiempo_final    = datetime.datetime(2016, 3, 5, 10)

    import math
    # parametros del generador de senales
    amplitud    = 0.2
    fase        = 1
    frecuencia  = 20*math.pi

    generator   = Generador(amplitud, fase, frecuencia)
    
    #TODO construir un detector

    #TODO construir un nuevo radar


    # parametros para un blanco
    amplitud_de_frecuencia_del_blanco = amplitud + 100
    tiempo_inicial_del_blanco = datetime.datetime(2016, 3, 5, 2)
    tiempo_final_del_blanco = datetime.datetime(2016, 3, 5, 4)

    target_alpha = Blanco(amplitud_de_frecuencia_del_blanco,\
    tiempo_inicial_del_blanco,tiempo_final_del_blanco)

    signal      = generator.generar(tiempo_inicial, tiempo_final)
    # the reflected signal is a list
    ref_alpha   = target_alpha.reflejar(signal,tiempo_inicial,tiempo_final)


    #TODO contruir un medio

    #TODO construir un radar

if __name__ == "__main__":
    main()
