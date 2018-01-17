#######################################################
# teste dos if aplicado em um cadastro                #
# By: Bruno Nasc                                      #
#                                                     #
#                                                     #
# Cadastro para ter acesso a uma pagina,..            #
#######################################################

######################################################
#          MODIFICAÇÃO DO CODIGO                     #
######################################################
#DATA   MODIFICAÇÃO
#######.##############################################
#
#180115 TESTE DO CODIGO COM MARIO. Bom dica do Mario
#      (cada modificação no codigo deve ser relatada
#       e codigo deve esta mas explicado possivel para
#      futuras manutenção)


# dados que serao manipulados
# variaveis globais
nome    = ''    # nome do cliente
snome   = ''    # sobrenome do usuario
login   = ''    # login para acesso
dataNas = ''    # data de nascimento
senha   = ''    # senha para acesso
Csenha  = ''    # confirmacao de senha
#tam_min_senha = 8  # tamanho minimo para senha


########## MENU PARA CAPTURAR DADOS ##########
## parametro msg: mensagem a ser exibida
def show_menu(msg):
    # seta como variaveis globais
    global nome
    global snome
    global login
    global dataNas
    global senha
    global Csenha

    print ("-------------------------------------------")
    print (msg)
    print ("-------------------------------------------")
    print ()
    nome    = str(input("Seu primeiro nome: "))
    snome   = str(input("Seu segundo nome: "))
    login   = str(input("Escolha o seu login: "))
    dataNas = input("Sua data de Nascimento. Ex: dd/mm/ano. : ")
    senha   = str(input("Escolhao sua senha: "))
    Csenha  = str(input("Confirme sua senha: "))
    print ()


########## MENU PARA MOSTRAR QUE O CADASTRO FOI EFETUADO COM SUCESSO ##########
def show_cadastro_sucesso(nome, snome, login, senha):
    print("---------------")
    print ("Senha aceita!")
    print("---------------")
    print ("Bem vindo:",nome,snome )
    print ("Seu login é:",login)
    print ("E sua senha é : ",senha)
    print ("ATENÇÃO: Mantenha sua senha em SEGURANÇA !!!")


########## VERIFICA OS DADOS E 'CADASTRA' ##########
## senha deve ter no minimo 8 caracteres
def cadastra():
    # seta como variaveis globais
    global nome
    global snome
    global login
    global senha
    global Csenha
    tam_min_senha = 8  # tamanho minimo para senha
    tam_senha = len(senha)

    if(tam_senha >= tam_min_senha):
        if (senha==Csenha):
            show_cadastro_sucesso(nome, snome, login, senha)
        else:
            show_menu("Senha não confere. Tente novamente!")
            cadastra()
    else:
        show_menu("Senha deve ter no minimo 8 caracteres. Tente novamente")
        cadastra()


#############################################################
############# INICIO DO PRORAMA #############################
#############################################################
show_menu("-------BEM VINDO! Tela de cadastro---------")
cadastra()