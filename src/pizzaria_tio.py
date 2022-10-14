#ingredientes em um dataframe


#Pizza
######################################
#Tipo           Ingredientes  Valor
#Massa      Tradicional     1
#Molho      Tomate          1
#Queijo     Mussarela       1 
#Cobertura  Azeitona        1
#Total                      4

#Ingredientes
########################################################
#Tipo                    Nome        Valor       
#Massa              Tradicional  5            
#Massa               ----        4            
#Molho               ----        -  
#Molho               ----
#Queijo              ----
#Queijo              ----   
#Cobertura           ----
#Cobertura           ----   

#Monta pizzas, Cadastra Ingredientes, Remove Ingredientes, Lista Ingredientes (+++)

def listar_ingredientes(ingredientes, tipo=""):

    # imprime a lista de ingredientes e retorna a lista de ingrediente selecionada/filtrada
    pass

def cadastrar_ingrediente(ingredientes, tipo ,nome, valor):

    # Retorna o dataframe atualizado, mas imprime o ingrediente adicionado
    pass

def remover_ingrediente(ingredientes, nome_ingrediente):
    """
    Função que remove o ingrediente selecionado por meio do nome

    :param ingredientes: Dataframe contendo as informações de todos os ingredientes
    :type ingredientes: panda.core.Dataframe
    :param nome_ingrediente: Nome do ingrediente a ser removido
    :type nome_ingrediente: str
    :return: Dataframe atualizado, e uma print no console do ingrediente removido
    :rtype: panda.core.Dataframe
    """
    # Retorna o dataframe atualizado, mas imprime o ingrediente removido
    pass

def montar_pizza(ingredientes, massa, molho, queijo, cobertura):
    
    # retorna o valor da pizza, mas tambem imprimir o conteúdo/preço da pizza
    pass