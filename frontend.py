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
#do code here
    ui.run_with(app)


