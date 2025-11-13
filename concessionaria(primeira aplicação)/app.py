import os
#Importa o módulo os, usado aqui para limpar o terminal (os.system('cls') no Windows).

#dicionários
concessionarias =  [{'nome': 'Praça', 'categoria': 'importados', 'ativo':False}, 
                    {'nome': 'Barra', 'categoria': 'Sedan','ativo':True},
                    {'nome': 'Tijuca', 'categoria': 'Hact','ativo':False}]
#É uma lista de dicionários, onde cada dicionário representa uma concessionária com:
#'nome': nome da loja
#'categoria': tipo de carro (ex: Sedan, Hatch, Importado)
#'ativo': indica se está ativa (True) ou não (False)

def nome_programa():
    print(""" Concessionaria """)
#Exibe o nome do programa na tela.
#Usada no início da execução (dentro de main()).

def definir_opcoes():
    print('1. cadastrar concessionaria')
    print('2. listar concessionaria')
    print('3. ativar concessionaria')
    print('4. sair concessionaria\n')
#Mostra o menu principal com as opções que o usuário pode escolher.
#Não retorna nada; apenas exibe texto no terminal.

def sair_app():
    exibir_subtitulo('Sair do app')
    #os.system('cls')
    #os.system('clear') no mac
    #print('sair do app\n')
#Exibe um subtítulo “Sair do app”.
#Poderia encerrar o programa (mas não há exit() aqui, então apenas limpa a tela e mostra o título).
#Comentários sugerem que no futuro poderia ser implementado os.system('cls') e print('sair do app').

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()
#Espera o usuário apertar uma tecla e chama novamente main(), voltando ao menu principal.
#É o ponto de retorno usado por várias funções após executar uma ação.

def opcao_invalida():
    print('opção invalida!\n')
    voltar_ao_menu_principal()
    #input('Digite uma tecla para voltar ao menu principal!')
#Exibida quando o usuário escolhe uma opção que não existe ou digita algo inválido.
#Depois de avisar, chama voltar_ao_menu_principal() para retornar ao menu.

#refatorando o código
def exibir_subtitulo(texto):
    os.system('cls')
    #print(texto)
    #print()
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()
#Limpa a tela (cls no Windows).
#Exibe o texto passado com uma moldura de asteriscos para destacar o subtítulo.
#Exemplo de saída:
#**************
#Listando concessionaria
#**************

def cadastrar_nova_concessionaria():
    exibir_subtitulo('Cadastro de novas concessionarias')
    #os.system('cls')
    #print('Cadastro de novos concessionaria\n')
    nome_da_concessionaria = input('Digite o nome da nova concessionaria que deseja cadastrar:')
    categoria = input(f'Digite o nome categoria {nome_da_concessionaria}: ')
    #concessionarias.append(nome_da_concessionaria)
    dados_concessionaria = {'nome':nome_da_concessionaria, 'categoria': categoria, 'ativo':False }
    concessionarias.append(dados_concessionaria)
    print(f'A concessionaria {nome_da_concessionaria} foi cadastrado com sucesso\n')
    #input('Digite uma tecla para voltar ao menu principal: ')
    #main()
    voltar_ao_menu_principal()
#Mostra o subtítulo de cadastro.
#Pede ao usuário o nome e a categoria da nova concessionária.
#Cria um novo dicionário com os dados e o adiciona à lista global concessionarias.
#Confirma o cadastro e volta ao menu principal.

def listar_concessionarias():
        exibir_subtitulo('Listando concessionaria')
        #os.system('cls')
        #print('listando todas as concessionarias\n')
        #para cada concessionaria na lista concessionarias
        for concessionaria in concessionarias:
            nome_concessionaria = concessionaria['nome']
            categoria = concessionaria['categoria']
            ativo = 'ativado' if concessionaria['ativo'] else 'desativado'
            print(f'- {nome_concessionaria} | {categoria} | {ativo}')
            #print(f'- {concessionaria}\n') 
            #input('\nDigite uma tecla para voltar ao menu principal: ')
            #main()
        voltar_ao_menu_principal()
#Mostra um subtítulo e lista todas as concessionárias.
#Para cada item da lista concessionarias, exibe:
#- Barra | Sedan | ativado
#Usa operador ternário para mostrar “ativado” ou “desativado”.
#Retorna ao menu após a listagem.

def  ativar_concessionaria():
    exibir_subtitulo('ALterando estado da concessionaria')
    nome_concessionaria = input('Digite o nome da concessionaria de deseja alterar o estado ') 
    concessionaria_encontrado = False
    #para cada concessionaria na lista concessionarias
    for concessionaria in concessionarias:
        if nome_concessionaria == concessionaria['nome']:
           concessionaria_encontrado = True
           concessionaria['ativo'] = not concessionaria['ativo']
           mensagem = f'A concessionaria {nome_concessionaria} foi ativado com sucesso' if concessionaria['ativo'] else f'O restaurante {nome_concessionaria} foi desativado com sucesso'
           print(mensagem)
    if not concessionaria_encontrado:
        print('A concessionaria não foi encontrado')       
    voltar_ao_menu_principal()
#Permite ativar ou desativar uma concessionária já cadastrada.
#O usuário digita o nome; o programa percorre a lista:
#Se encontrar, inverte o valor de ativo (True ↔ False).
#Exibe uma mensagem informando o novo estado.
#Se não encontrar, exibe aviso de erro.
#Volta ao menu principal no final.

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        #opcao_escolhida = int(opcao_escolhida)
        #print(opcao_escolhida ==1)
        #print(type(opcao_escolhida))
        #print(type(1))
        #print('Você escolha a opção', opcao_escolhida)
        if opcao_escolhida ==1:
                #print('cadastrar concessionaria')
                cadastrar_nova_concessionaria()
        elif opcao_escolhida ==2:
                #print('listar concessionaria')
                listar_concessionarias()
        elif opcao_escolhida ==3:
                #print('ativar concessionaria')
                ativar_concessionaria()
        elif opcao_escolhida ==4:
                sair_app()
        else:
            opcao_invalida()
    except:
            opcao_invalida()
#Lê a opção escolhida pelo usuário no menu.
#Usa try/except para capturar erros (ex: se o usuário digitar letra).
#Executa a função correspondente:
#Cadastrar nova concessionária
#Listar concessionárias
#Ativar/desativar
#Sair
#Qualquer outra opção chama opcao_invalida().

def main():
    os.system('cls')
    nome_programa()
    definir_opcoes()
    escolher_opcoes()
#Função principal que:
#Limpa a tela
#Exibe o nome do programa
#Mostra o menu
#Chama escolher_opcoes() para processar a escolha
  
if __name__ == '__main__':
    main()
#Faz com que o programa execute o menu automaticamente quando o arquivo for rodado diretamente.
#Evita que o menu seja executado se o arquivo for apenas importado em outro módulo.