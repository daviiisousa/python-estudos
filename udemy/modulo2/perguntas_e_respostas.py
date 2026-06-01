perguntas = [
    {
        'pergunta': 'Qual é a capital da França?',
        'opcoes': ['Paris', 'Londres', 'Berlim', 'Madrid'],
        'resposta_correta': 'Paris'
    },
    {
        'pergunta': 'Qual é o maior planeta do sistema solar?',
        'opcoes': ['Terra', 'Júpiter', 'Saturno', 'Marte'],
        'resposta_correta': 'Júpiter'
    },
    {
        'pergunta': 'Quem pintou a Mona Lisa?',
        'opcoes': ['Leonardo da Vinci', 'Pablo Picasso', 'Vincent van Gogh', 'Michelangelo'],
        'resposta_correta': 'Leonardo da Vinci'
    }
]

acertadas = 0

for pergunta in perguntas:
    print()
    print(pergunta['pergunta'])
    print()
    for i, opcao in enumerate(pergunta['opcoes']):
        print(f"{i}) {opcao}")
    print()
    try:
        resposta_usuario = int(input("Digite o número da resposta correta: "))
        if pergunta['opcoes'][resposta_usuario] == pergunta['resposta_correta']:
            print()
            print("Resposta correta!")
            acertadas += 1
        else:
            print()
            print("Resposta incorreta.")
    except (ValueError, IndexError):
        print()
        print("Entrada inválida. Por favor, digite um número válido.")
        
print(f"Você acertou {acertadas} de {len(perguntas)} perguntas.")

