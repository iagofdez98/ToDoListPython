# coding: utf-8
# Nueva tarea

import webapp2
import time
from webapp2_extras import jinja2
from datetime import datetime
from model.tarea import Tarea


class NuevaTareaHandler(webapp2.RequestHandler):
    def get(self):
        valores_plantilla = {
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("nueva_tarea.html", **valores_plantilla))

    def post(self):
        nombre = self.request.get("edNombre", "")
        descripcion = self.request.get("edDescripcion", "")
        str_fecha = self.request.get("edFecha", "")
        todo = "Pendiente"

        fecha = datetime.strptime(str_fecha, '%Y-%m-%d')

        tarea = Tarea(nombre=nombre, descripcion=descripcion, fecha=fecha, todo=todo)
        tarea.put()
        time.sleep(1)
        return self.redirect("/")


app = webapp2.WSGIApplication([
    ('/tareas/nueva', NuevaTareaHandler)
], debug=True)
