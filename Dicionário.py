Cumprimentos = {
                'Good morning': {
                    'alternativas': ['Boa noite', 'Obrigado', 'Bom dia', 'Até logo'],
                    'resposta': 'Bom dia'
                },
                'Hello': {
                    'alternativas': ['Olá', 'Boa tarde', 'Tchau', 'Adeus'],
                    'resposta': 'Olá'
                },
                'Boa noite': {
                    'alternativas': ['Good morning', 'Goodbye', 'Excuse me', 'Good evening'],
                    'resposta': 'Good evening'
                },
                'Good afternoon': {
                    'alternativas': ['Boa tarde', 'Good morning', 'See you later', 'Hello'],
                    'resposta': 'Boa tarde'
                },
                'Tchau': {
                    'alternativas': ['Please', 'Hi', 'Bye', 'Maybe'],
                    'resposta': 'Bye'
                },
                'See you soon': {
                    'alternativas': ['Até logo', 'Boa noite', 'Hello', 'Good afternoon'],
                    'resposta': 'Até logo'
                },
                'Welcome': {
                    'alternativas': ['Obrigado', 'Bem-vindo', 'Até logo', 'Com liceça'],
                    'resposta': 'Bem-vindo'
                },
                'Desculpa': {
                    'alternativas': ['Maybe', 'Thank you', 'I dont know', 'Sorry'],
                    'resposta': 'Sorry'
                },
                'Excuse me': {
                    'alternativas': ['Com licença', 'Tchau', 'Me ajude', 'Talvez'],
                    'resposta': 'Com licença'
                },
                'Thank you': {
                    'alternativas': ['Não sei', 'Desculpa', 'Obrigado', 'Te amo'],
                    'resposta': 'Obrigado(a)'
                }}
Cores = {'Blue': {'alternativas': ['Verde', 'Azul', 'Amarelo', 'Preto'], 'resposta': 'Azul'
                  },
         'Orange': {'alternativas': ['Amarelo', 'Marrom', 'Rosa', 'Laranja'], 'resposta': 'Laranja'
                    },
         'Yellow': {'alternativas': ['Amarelo', 'Preto', 'Vermelho', 'Cinza'], 'resposta': 'Amarelo'
                    }
         }
Assuntos = ['Cumprimentos', 'Cores']
assunto = Assuntos
print(assunto)
for a in assunto:
    print(type(a))

Modulos = [Cumprimentos, Cores]

