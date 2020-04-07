from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from Controller.MatrixCell import MatrixCell
from DataObject import Matrix

Builder.load_file('View/matrixview.kv')

class MatrixView(GridLayout):
    def __init__(self, **kwargs):
        super(MatrixView, self).__init__()
        self.matrix = kwargs.get('matrix', None)
        self.cols = self.matrix.size[0]
        self.initialize()

    def initialize(self):
        for i in range(self.matrix.size[0]):
            for j in range(self.matrix.size[1]):
                self.add_widget(MatrixCell(value=self.matrix.matrix[i][j]))







