from reactpy import component, html, hooks
from reactpy.backend.fastapi import configure
from fastapi import FastAPI

@component
def Item(text, initial_done=False):
  done, set_done = hooks.use_state(initial_done)
  
  def handle_click(event):
    set_done(not done)
    
  attrs={ "style": {"color": "green"}} if done else {}
  
  if done:
    return html.li(attrs, text)
  else:
    return html.li(
      html.li(attrs, text),
      html.button({"onClick": handle_click}, "Marcar como completada")
    )

@component
def HelloWorld():
    return html._(
      html.h1("Lista de tareas"),
      html.ul(
        Item("Tarea 1"),
        Item("Tarea 2"),
        Item("Tarea 3", initial_done=True),
      )
    )
    
app = FastAPI()
configure(app, HelloWorld)