from django.http import HttpResponse
import datetime
def diaDeHoy(request):

        dia = datetime.datetime.now()

        documentoDeTexto = f"Hoy es día: <br> {dia}"

        return HttpResponse(documentoDeTexto)



def miNombreEs(self, nombre):

      documentoDeTexto = f"Mi nombre es: <br><br>  {nombre}"
      return HttpResponse(documentoDeTexto)

from django.template import Template, Context
def probandoTemplate(self):

    miHtml = open("/Users/Tavo/Documents/PythonProyecto1/Proyecto1/Proyecto1/plantillas/index.html")

    plantilla = Template(miHtml.read()) #Se carga en memoria nuestro documento, template1   
    ##OJO importar template y contex, con: from django.template import Template, Context

    miHtml.close() #Cerramos el archivo

    miContexto = Context() #EN este caso no hay nada ya que no hay parametros, IGUAL hay que crearlo

    documento = plantilla.render(miContexto) # Aca renderizamos la plantilla en documento

    return HttpResponse(documento)