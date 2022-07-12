class Author:
    def __init__(self,id,name,birthday,description):
        self._id = id
        self._name = name
        self._bithday = birthday
        self._description = description
    
    def printAuthor(self):
        print(self._name)

class Author_Artwork:
    def __init__(self,idAuthor,idArtwork):
        self._idAuthor = idAuthor
        self._idArtwork = idArtwork
