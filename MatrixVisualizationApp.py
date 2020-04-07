
from kivy.app import App
from kivy.config import Config
from kivy.uix.screenmanager import Screen, ScreenManager

from Controller.WindowFileDropView import WindowFileDropView

Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '768')

class ScreenWindowFileDrop(Screen):
    def __init__(self, **kwargs):
        super(ScreenWindowFileDrop, self).__init__(**kwargs)
        self.add_widget(WindowFileDropView())

class MatrixVisualizationApp(App):
    def __init__(self):
        App.__init__(self)

    def build(self):
        return screen_manager


screen_manager = ScreenManager()
screen_manager.add_widget(ScreenWindowFileDrop())
matrix_visualization = MatrixVisualizationApp()

matrix_visualization.run()
