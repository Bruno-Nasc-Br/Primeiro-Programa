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




########## INICIO DO PROGRAMA ##########
print ("-------------------------------------------")
print ("-------BEM VINDO! Tela de cadastro---------")
print ("-------------------------------------------")
print ()
nome = str(input("Seu primeiro nome: "))
snome = str(input("Seu segundo nome: "))
login = str(input("Escolha o seu login: "))
dataNas = input("Sua data de Nascimento. Ex: dd/mm/ano. : ")
senha = str(input("Escolhao sua senha: "))
Csenha = str(input("Confirme sua senha: "))
print ()

if (senha==Csenha):
    print("---------------")
    print ("Senha aceita!")
    print("---------------")
    print ("Bem vindo:",nome,snome )
    print ("Seu login é:",login)
    print ("E sua senha é : ",senha)
    print ("ATENÇÃO: Mantenha sua senha em SEGURANÇA !!!")

else:
    print ("==================================")
    print ("Senha não confere. Tente novamene!")
    print("===================================")
    print ("________Segunda tentativa_________")
    nome = str(input("Seu primeiro nome: "))
    snome = str(input("Seu segundo nome: "))
    login = str(input("Escolha o seu loging: "))
    dataNas = input("Sua data de Nascimento. Ex: dd/mm/ano. : ")
    senha = input("Escolhao sua senha: ")
    Csenha = input("Confirme sua senha: ")

if (senha == Csenha):
     print (" Agora seu cadastro foi concluido !")
     print("-----------------------------------")
     print ("Senha aceita!")
     print ("----------------------------------")
     print ("Bem vindo:",nome,snome)
     print ("seu login é: ",login)
     print ("E sua senha é: ",senha)
     print ("ATENÇÃO: Mantenha sua senha em SEGURANÇA !!!")














