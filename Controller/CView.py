
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup

from Controller.MatrixView import MatrixView
from DataObject import CMatrix



Builder.load_file('View/cview.kv')

class CView(BoxLayout):

    cmatrix = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(CView, self).__init__()
        self.bind(cmatrix=self.refresh)
        self.cmatrix = kwargs.get('cmatrix', None)
        self.allow_popup = kwargs.get('allow_popup', True)

    def refresh(self, instance, value):
        if self.cmatrix is not None and self.cmatrix.size > 0:
            self.add_widget(MatrixView(matrix=self.cmatrix.cvalue))
            self.add_widget(Label(text='=', size_hint=(0.4,1)))
            self.add_widget(MatrixView(matrix=self.cmatrix.matrices[0] * self.cmatrix.pattern[0]))
            for i in range(1,self.cmatrix.size):
                self.add_widget(Label(text="+", size_hint=(0.2,1)))
                self.add_widget(MatrixView(matrix=(self.cmatrix.matrices[i] * self.cmatrix.pattern[i])))

    def zoom(self, touch):
        if self.allow_popup and touch.button == 'left' and self.collide_point(touch.x, touch.y):
            popup = Popup(title='C Matrix View',content=CView(cmatrix=self.cmatrix, allow_popup=False),size_hint=(1,0.3))
            popup.open()







