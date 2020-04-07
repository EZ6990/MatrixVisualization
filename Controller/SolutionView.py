
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

from Controller.CView import CView
from Controller.MatrixView import MatrixView
from DataObject import CMatrix

Builder.load_file('View/solutionview.kv')

class SolutionView(BoxLayout):

    solution = ListProperty([])

    def __init__(self, **kwargs):
        super(SolutionView, self).__init__()
        self.bind(solution=self.refresh)
        self.solution = kwargs.get('solution', [])

    def refresh(self, instance, value):
        self.clear_widgets()
        if len(self.solution) > 0:
            for cmatrix in self.solution:
                self.add_widget(CView(cmatrix=cmatrix))

    def set_solution(self,solution):
        self.solution = solution






