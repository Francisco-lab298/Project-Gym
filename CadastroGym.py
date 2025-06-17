import string


def registroGym():
    nome = str(input("Digite seu nome: "))#teste
    QualSeuSexo = input("Qual o seu sexo? [masculino] [feminino]: ")
    if QualSeuSexo == "masculino":
        print("Homem")
    elif QualSeuSexo == "feminino":
        print("Mulher")
    else:
        while True:
            print("Somente masculino ou feminino")
            QualSeuSexo = input("Qual o seu sexo? [masculino] [feminino]: ")
            if QualSeuSexo == "masculino":
                print("Homem")
                break
            elif QualSeuSexo == "feminino":
                print("Mulher")
                break

    idade = int(input("Sua Idade atual: "))#int para só deixar entra numero /  input so solicita info

    QuerTomarSuplemento = input("Quer tomar suplemento [sim] [não]: ")#questionamento
    if QuerTomarSuplemento == "sim":#se ele quiser em baixo vai ter mensagem
        print("Suplementará")#mensagem aviso
    elif QuerTomarSuplemento == "não":#se ele não quiser em baixo vai ter mensagem
        print("Somente treino")#mensagem aviso
    else:
        while True:
            print("Preencha somente (sim ou não)")
            QuerTomarSuplemento = input("Quer tomar suplemento [sim] [não]: ")
            if QuerTomarSuplemento == "sim":
                print("Homem")
                break
            elif QuerTomarSuplemento == "não":
                print("Somente treino")
                break

    altura = float(input("Sua Altura: "))#Float representa numero em casas decimais
    print(f"{altura:}")
    peso = int(input("Qual o seu peso: "))
    email = str(input("Digite seu e-mail: "))
registroGym()