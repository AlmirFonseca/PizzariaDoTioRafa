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
    """Lista os ingredientes do DataFrame recebido do tipo especificado, se definido
    
    :param ingredientes: O DataFrame que contém os ingredientes, com colunas Tipo, Nome, Valor
    :type ingredientes: pandas.core.DataFrame
    :param tipo: Tipo de ingredientes a serem listados
    :type tipo: str
    :return: O DataFrame filtrado pelo tipo selecionado
    :rtype: pandas.core.DataFrame
    """
    pass

def cadastrar_ingrediente(ingredientes, tipo ,nome, valor):

    # Retorna o dataframe atualizado, mas imprime o ingrediente adicionado
    pass

def remover_ingrediente(ingredientes, nome_ingrediente):

    # Retorna o dataframe atualizado, mas imprime o ingrediente removido
    pass

def montar_pizza(ingredientes, massa, molho, queijo, cobertura):
    
    # retorna o valor da pizza, mas tambem imprimir o conteúdo/preço da pizza
    pass