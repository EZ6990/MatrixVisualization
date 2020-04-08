
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

from Controller.MatrixView import MatrixView
from DataObject import CMatrix

Builder.load_file('View/cview.kv')

class CView(BoxLayout):


    cmatrix = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(CView, self).__init__()
        self.bind(cmatrix=self.refresh)
        self.cmatrix = kwargs.get('cmatrix', None)

    def refresh(self, instance, value):
        if self.cmatrix is not None and self.cmatrix.size > 0:
            self.add_widget(MatrixView(matrix=self.cmatrix.cvalue))
            self.add_widget(Label(text='=', size_hint=(0.4,1)))
            self.add_widget(MatrixView(matrix=self.cmatrix.matrices[0] * self.cmatrix.pattern[0]))
            for i in range(1,self.cmatrix.size):
                self.add_widget(Label(text="+", size_hint=(0.2,1)))
                self.add_widget(MatrixView(matrix=(self.cmatrix.matrices[i] * self.cmatrix.pattern[i])))








