class Blanco(object):
    """
    Define un blanco a ser detectado por un radar
    """

    def __init__(self, amplitud, tiempo_inicial, tiempo_final):
        self.amplitud       = amplitud
        self.tiempo_inicial = tiempo_inicial
        self.tiempo_final   = tiempo_final
        return

    def reflejar(self, senal, tiempo_inicial, tiempo_final):
        """
        try to intersect intervals
        signal is the list returned by generador.generar()

        """
        inf_interval = max(tiempo_inicial, self.tiempo_inicial)
        sup_interval = min(tiempo_final, self.tiempo_final)
        reflection   = list(l)
        if inf_interval <= sup_interval:
            for i in range(inf_interval,sup_interval+1):
                reflection[i] = senal[i]*self.amplitud
        return reflection