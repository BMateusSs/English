from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from Dicionário import Modulos
from kivy.uix.image import Image


class TelaEstudo(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        fundo = Image(source='fundo2.png', allow_stretch=True, keep_ratio=False)
        self.add_widget(fundo)

        self.i = 0

        self.categoria = None

        self.organizar_botoes = BoxLayout(orientation='vertical',
                                          spacing=10,
                                          size_hint=(None, None),
                                          pos_hint={'center_x': 0.5, 'y': 0.2})

        self.add_widget(self.organizar_botoes)

        self.exibir_expressão = Label(text='',
                                      font_size=30,
                                      pos_hint={'center_x': 0.5, 'y': 0.3})

        self.add_widget(self.exibir_expressão)

        self.modulo = Modulos

    def mudar_modulo(self, indice):
        self.categoria = self.modulo[indice]
        self.atividade()

    def atividade(self):
        print(self.i)

        self.organizar_botoes.clear_widgets()
        self.exibir_expressão.clear_widgets()

        if self.i < 3:
            self.expressão = list(self.categoria.keys())
            self.exibir_expressão.text = self.expressão[self.i]

            for alternativa in self.categoria[self.expressão[self.i]]['alternativas']:
                botao = Button(text=alternativa,
                               size_hint=(None, None),
                               size=(100, 50),
                               background_color=(1, 1, 1, 1),
                               background_normal='botao.png')
                self.organizar_botoes.add_widget(botao)
                botao.bind(on_press=self.acertou)
        else:
            self.mensagem_final()

    def acertou(self, texto):
        if texto.text == self.categoria[self.expressão[self.i]]['resposta']:
            self.exibir_expressão.text = 'Você acertou!'
            texto.background_color = (0, 1, 0, 1)
        else:
            self.exibir_expressão.text = 'Você errou!'
            texto.background_color = (1, 0, 0, 1)
        self.i += 1
        Clock.schedule_once(lambda dt: self.atividade(), 2)

    def mensagem_final(self):
        self.i = 0
        self.organizar_botoes.clear_widgets()
        self.exibir_expressão.text = 'Você completou a lição!'
        Clock.schedule_once(lambda dt: self.retornar(), 2)

    def retornar(self):
        self.manager.current = 'tela1'

