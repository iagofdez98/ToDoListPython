# Tarea a guardar por un usuario

from google.appengine.ext import ndb


class Tarea(ndb.Model):
    nombre = ndb.StringProperty(indexed=True)
    descripcion = ndb.StringProperty(required=True)
    fecha = ndb.DateTimeProperty(auto_now_add=True)
    todo = ndb.StringProperty(required=True)

    @staticmethod
    def recupera(req):
        try:
            id = req.GET["id"]
        except KeyError:
            id = ""

        return ndb.Key(urlsafe=id).get()

