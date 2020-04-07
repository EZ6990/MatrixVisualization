
from kivy.lang import Builder
from kivy.properties import ListProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

from Controller.CView import CView
from Controller.MatrixView import MatrixView
from Controller.SolutionView import SolutionView
from DataObject import CMatrix

Builder.load_file('View/solutionsview.kv')

class SolutionsView(BoxLayout):

    solutions = ListProperty([])
    solution = ObjectProperty(None)

    def __init__(self, **kwargs):
        self.presented_index = 0
        super(SolutionsView, self).__init__()
        self.bind(solutions=self.refresh_solutions)
        self.solutions = kwargs.get('solutions', [])

    def refresh_solutions(self, instance, value):
        if len(self.solutions) > 0:
            self.refresh_solution()

    def refresh_solution(self):
        self.solution.set_solution(self.solutions[self.presented_index])


    def previous_index(self):
        self.presented_index -= 1
        if -self.presented_index < len(self.solutions):
            self.presented_index = 0
        self.refresh_solution()

    def next_index(self):
        self.presented_index += 1
        if self.presented_index >= len(self.solutions):
            self.presented_index = 0
        self.refresh_solution()










