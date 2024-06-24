from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from TelaUm import TelaInicial
from TelaDois import TelaEstudo


class English(App):
    def build(self):
        Window.size = (290, 560)
        gerenciador = ScreenManager()
        gerenciador.add_widget(TelaInicial(name='tela1'))
        gerenciador.add_widget(TelaEstudo(name='tela2'))

        return gerenciador


if __name__ == '__main__':
    English().run()
