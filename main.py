import nicegui
from nicegui import ui
import platform
import os
osmodel = platform.system()
ui.icon('thumb_up')
#add a button that plays Rick Astley's Never Gonna Give You Up
ui.button('Never Gonna Give You Up',on_click=lambda: ui.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ'))
ui.label('Your operating system is ' + osmodel)
app = ui.run(port=8000)
