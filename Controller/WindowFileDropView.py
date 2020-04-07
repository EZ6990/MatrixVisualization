
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

from Controller.SolutionsView import SolutionsView
from Model.PicatSolutionsLoader import get_solutions

Builder.load_file('View/windowfiledropview.kv')

class WindowFileDropView(BoxLayout):

    def __init__(self, **kwargs):
        super(WindowFileDropView, self).__init__()
        Window.bind(on_dropfile=self._on_file_drop)

    def _on_file_drop(self, window, file_path):
        self.clear_widgets()
        solutions = get_solutions(file_path)
        self.add_widget(SolutionsView(solutions=solutions))








