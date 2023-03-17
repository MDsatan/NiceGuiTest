import nicegui
from nicegui import ui
import platform
import uvicorn
import asyncio
from fastapi import FastAPI
from nicegui import ui
osmodel = platform.system()

def init(app: FastAPI) -> None:
    @ui.page('/show')
    def show():
        ui.label('Hello, RickRoller!', style='h1')
        ui.icon('thumb_up')
        #add GIF with rickroll
        ui.image('https://media.tenor.com/x8v1oNUOmg4AAAAM/rickroll-roll.gif', )
        ui.button('Never Gonna Give You Up',on_click=lambda: ui.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ'))
        ui.label('Your operating system is ' + osmodel)
    ui.run_with(app)


