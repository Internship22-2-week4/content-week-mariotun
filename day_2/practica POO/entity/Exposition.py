class Exposition:
    def __init__(self,id,name,date,place,description):
        self._id = id
        self._name = name
        self._date = date
        self._place = place
        self._description = description
        self._briefcase = []
    '''
    def __repr__(self):
        return str(self.__dict__)'''
    
    def addArtwork(self,artwork):
        self._briefcase.append(artwork)

    def getArtworks(self):
        try:
            print("*"*20+" Exposicion "+"*"*20)
            print("Id: {}, Nombre: {}".format(self._id,self._name))
            for element in self._briefcase:
                    print("Obra: {}, Tipo: {}, Precio: {}".format(element._name,element._type._name,element._price))
                # print("*"*50)
        except:
            print("Error: Verifique que la obra de arte exista")


class Briefcase:
    def __init__(self,id,name,description):
        self._id = id
        self._name = name
        self._description = description
        self._artwork = []


    def  addArtwork(self,artwork):
        self._artwork.append(artwork)
    
    def getById(self,id):
        for element in self._artwork:
            if element._id == id:
                return element

    
    def getArtworks(self):
        try:
            print("*"*20+" Portafolio "+"*"*20)
            for element in self._artwork:
                print(element._id,"---> "+element._name)
        except:
            print("Error al mostrar el portafolio")
