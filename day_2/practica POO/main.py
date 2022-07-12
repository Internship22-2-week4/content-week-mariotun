from entity.Author import Author,Author_Artwork
from entity.Multimedia import Multimedia,Type
from entity.Artwork import Artwork
from entity.Exposition import Briefcase,Exposition

autor1 = Author(10,"rafael estrada","05/08/1985","especializado en pintura")
autor2 = Author(20,"carlos rodriguez","12/03/1990","especializado en escultura")
autor3 = Author(30,"sofia lopez","24/11/1992","especializada en fotografia")

multimedia1 = Multimedia(1,"pintura oceano","www.pintura1.com","representa tranquilidar")
multimedia2 = Multimedia(2,"video escultura","www.video1.com","video con tomas desde el aire")

tipoEscultura = Type(100,"Escultura","Realizar con materiales madera o hielo")
tipoVideo = Type(200,"Video","No exceder los 20 minutos")
tipoPintura = Type(300,"Pintura","Que represente a la ciudad de guatemala")

artwork1 = Artwork(1,"la paz","07/10/2015",300,"Hecho con materiales de calidad",tipoVideo,multimedia2)
artwork2 = Artwork(2,"luz en la vida","17/12/2014",500,"Ejemplo de personas perseverantes",tipoVideo,multimedia1)
artwork3 = Artwork(3,"amor verdadero","25/05/2017",730,"Escultura de hielo",tipoEscultura,multimedia1)
artwork4 = Artwork(4,"corazon feliz","11/09/2016",460,"Basado en personas enamoradas",tipoVideo,multimedia2)
artwork5 = Artwork(5,"la naturaleza","21/04/2015",1200,"Inspirado en peten",tipoPintura,multimedia2)

Autor_Obra1 = Author_Artwork(1,4)
Autor_Obra2 = Author_Artwork(2,5)
Autor_Obra3 = Author_Artwork(3,1)

BriefcaseOriginal = Briefcase(20,"Portafolio ganador","Obras de arte con mas vistas")
BriefcaseOriginal.addArtwork(artwork1)
BriefcaseOriginal.addArtwork(artwork2)
BriefcaseOriginal.addArtwork(artwork3)
BriefcaseOriginal.addArtwork(artwork4)
BriefcaseOriginal.addArtwork(artwork5)
BriefcaseOriginal.getArtworks()

exposicionMario = Exposition(30,"exposicion de Mario","24/10/2022","zona 1","desde las 5:00 pm")
exposicionMario.addArtwork(BriefcaseOriginal.getById(1))
exposicionMario.addArtwork(BriefcaseOriginal.getById(2))
exposicionMario.getArtworks()

exposicionLucia = Exposition(31,"exposicion de Lucia","12/08/2022","zona 1","desde las 5:00 pm")
exposicionLucia.addArtwork(BriefcaseOriginal.getById(2))
exposicionLucia.addArtwork(BriefcaseOriginal.getById(4))
exposicionLucia.addArtwork(BriefcaseOriginal.getById(5))
exposicionLucia.getArtworks()

