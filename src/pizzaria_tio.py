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

    # Retorna o dataframe atualizado, mas imprime o ingrediente removido
    pass

def montar_pizza(ingredientes, massa, molho, queijo, cobertura):
    """
    Função que monta a pizza

    A função recebe a lista de ingredientes, e os ingredientes escolhidos pelo usuario:
    a massa, o molho, o queijo e a cobertura. A função computa o valor da pizza e imprime
    a pizza selecionada e o valor da pizza. A função retorna o dataframe com a estrutura da pizza, 
    contendo também o seu valor total.
    Caso algum ingrediente selecionado não exista, o ingrediente não é computado.

    :param ingredientes: DataFrame com os ingredientes disponíveis
    :type ingredientes: pandas.core.DataFrame
    :param massa: o nome da massa escolhida
    :type massa: str
    :param molho: o nome do molho escolhid
    :type molho: str
    :param queijo: o nome do queijo escolhido
    :type queijo: str
    :param cobertura: o nome da cobertura escolhida
    :type cobertura: str
    :rtype: pandas.core.DataFrame
    
    """
    
    # retorna o valor da pizza, mas tambem imprimir o conteúdo/preço da pizza
    pass