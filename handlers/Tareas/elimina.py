# coding: utf-8
# Elimina tarea

import webapp2
import time

from model.tarea import Tarea


class EliminaTareaHandler(webapp2.RequestHandler):
    def get(self):
        tarea = Tarea.recupera(self.request)
        tarea.key.delete()
        time.sleep(1)

        return self.redirect("/")


app = webapp2.WSGIApplication([
    ('/tareas/elimina', EliminaTareaHandler)
], debug=True)
