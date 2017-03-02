class Medio(object):

    def __init__(self, blancos):
        self.blancos = blancos


    def reflejar(self, una_senal, tiempo_inicial, tiempo_final):
        """
        Los blancos en el medio reflejan la senal
   
		nota mental: un radar que va girando y para cada intervalo angular
		la (unica) senal se ve modificada en la slice correspondiente
					
						360/longitud de la lista senal
						
        """
        for tar in self.blancos:
        	tar.reflejar ....

        #TODO reflejar en un medio debe reflejar en todos los blancos de un medio
        #y devolver la senal reflejada
        pass
