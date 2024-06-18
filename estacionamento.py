'''
autora: aliny krebs
data de criacao 17/06/20024'''


# meu carro já esta cadastrado, e ficara junto com os futuros carros
carros = {
    'ABC-1234': {
        'marca': 'mazda',
        'cor': 'roxo purpurina',
        'proprietario': 'aliny krebs', 
        'modelo': 'miata'
    }
}

# funcao que mostra o menu para o usuario escolher as alternativas 
def menu():
    print("1 - estacionar veiculo")
    print("2 - retirar veiculo")
    print("3 - veiculos estacionados")
    print("4 - esta estacionado?")
    print("0 - sair")
    try:
        opt = int(input("selecione a opção: "))
        return opt  # teste para verificar se o usuario digitou corretamente

    except Exception as e:
        print("digitado errado, burro")

# o usuario digita as informacoes necessarias, e é adicionado a lista de dados, e o try exception é usado novamente
def add_carro():
    try:  
        placa = input("digite a placa do carro: ")
        marca = input("informe a marca: ")
        cor = input("informe a cor: ")
        proprietario = input("informe o proprietario: ")
        modelo = input("informe o modelo: ")

        dados = {"placa": placa, "marca": marca,"cor": cor, "proprietario": proprietario, "modelo": modelo}
        carros[placa] = dados
    except Exception as e:
        print("algo foi digitado errado {e}")

# usando a placa de algum carro ja cadastrado, é usado o .pop para remover todos os dados da lista de dados, novamente usando try exception, para verificaçao de erros
def remover_carro():
    try:
        placa = input("digite a placa do carro ")
        if placa in carros:
            carro = carros.pop(placa)
            print(f"o carro:{carro['placa']} foi removido")
        else:
            print("o carro não foi estacionado, ou ouve erro de digitacao")
        input("fecha os olhos e clica em qualquer lugar, para continuar ")   
    except Exception as e:
        print("algo foi digitado errado {e}")

# esta funcao pega os carros ja cadastrados, que estao na lista carros, e os exibe usando o for
def listar_carro():
    for placa, dados in carros.items():
        print(f"placa: {placa} - marca: {dados['marca']} - cor: {dados['cor']} - proprietario: {dados['proprietario']} - modelo: {dados['modelo']}")
    input("fecha os olhos e clica em qualquer lugar, para continuar ")

# digitando a placa do carro, é feita a procura da placa, e o codigo responde com sim ou nao a pergunta usando if e else 
def esta_estacionado():
    try:
        placa = input("digite a placa: ")
        if placa in carros:
            print("sim, está estacionado e seguro")
        else:
            print("nao, roubaram seu carro")
        input("fecha os olhos e clica em qualquer lugar, para continuar ")    

    except Exception as e:
        print("algo foi digitado errado {e}")


if __name__ == '__main__':
    while True:
        match menu():
            case 1:
                add_carro()
            case 2:
                remover_carro()
            case 3:
                listar_carro()
            case 4:
                esta_estacionado()
            case 0:
                break
 