from kivy.lang import Builder
from kivy.uix.label import Label


Builder.load_file('View/matrixcell.kv')


class MatrixCell(Label):

    def __init__(self, **kwargs):
        self.value = kwargs.get("value", 0)
        super(MatrixCell, self).__init__()

    def cellColor(self):
        if self.value > 0:
            return 0,1,0,1              #green
        elif self.value < 0:
            return 1,0,0,1              #red
        else:
            return 0.1,0.1,0.1,0.5      #gray
