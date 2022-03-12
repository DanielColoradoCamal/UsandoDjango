from django.http import HttpResponse
from django.template import Template, Context, loader
import datetime
def diaDeHoy(request):

        dia = datetime.datetime.now()

        documentoDeTexto = f"Hoy es día: <br> {dia}"

        return HttpResponse(documentoDeTexto)



def miNombreEs(self, nombre):

      documentoDeTexto = f"Mi nombre es: <br><br>  {nombre}"
      return HttpResponse(documentoDeTexto)



def probandoTemplate(self):

    nombre = "Daniel"
    apellido = "Colorado"
    notas = [10,9,5,7,4,9]
    diccionario ={"nombre": nombre, "apellido":apellido, "notas" : notas}

    plantilla = loader.get_template('index.html') #Se carga en memoria nuestro documento,
    documento = plantilla.render(diccionario) # Aca renderizamos la plantilla en documento

    return HttpResponse(documento)