from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.image import Image
from Dicionário import Assuntos


class TelaInicial(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        assunto = Assuntos
        print(assunto)
        fundo = Image(source='fundo.png', allow_stretch=True, keep_ratio=False)
        self.add_widget(fundo)

        layout = GridLayout(cols=2,
                            size_hint=(None, None),
                            pos_hint={'center_x': 0.3, 'y': 0.5},
                            spacing=50)
        for a in assunto:
            cumprimentos = Button(text=a,
                                  font_size=20,
                                  color=(0, 0, 0, 1),
                                  bold=True,
                                  size_hint=(None, None),
                                  size=(100, 50)
                                  )
            layout.add_widget(cumprimentos)

            cumprimentos.bind(on_press=self.mudar_tela)
        self.add_widget(layout)

    def mudar_tela(self, botao):
        if botao.text == 'Cumprimentos':
            indice = 0
        elif botao.text == 'Cores':
            indice = 1

        self.manager.current = 'tela2'
        self.manager.get_screen("tela2").mudar_modulo(indice)

