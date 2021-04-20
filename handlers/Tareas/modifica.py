# coding: utf-8
# Nueva tarea

import webapp2
import time
from webapp2_extras import jinja2
from datetime import datetime
from model.tarea import Tarea
from google.appengine.ext import ndb


class ModificaTareaHandler(webapp2.RequestHandler):
    def get(self):
        tarea = Tarea.recupera(self.request)

        valores_plantilla = {
            "tarea": tarea
        }

        tarea.key.delete()
        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("modifica_tarea.html", **valores_plantilla))

    def post(self):
        nombre = self.request.get("edNombre", "")
        descripcion = self.request.get("edDescripcion", "")
        str_fecha = self.request.get("edFecha", "")
        todo = self.request.get("edTodo", "Pendiente")

        fecha = datetime.strptime(str_fecha, '%Y-%m-%d')

        tarea = Tarea(nombre=nombre, descripcion=descripcion, fecha=fecha, todo=todo)
        tarea.put()
        time.sleep(1)
        return self.redirect("/")


app = webapp2.WSGIApplication([
    ('/tareas/modifica', ModificaTareaHandler)
], debug=True)
