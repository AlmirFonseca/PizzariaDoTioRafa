import pandas as pd

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
    
    >>> df = pd.DataFrame(data=[["Massa", "Tradicional", 5.0]], columns=["Tipo", "Nome", "Valor"])
    >>> listar_ingredientes(df, "Massa")
        Tipo         Nome  Valor
    0  Massa  Tradicional    5.0
        Tipo         Nome  Valor
    0  Massa  Tradicional    5.0
    
    """
    if tipo == "":
        ingredientes_filtrados = ingredientes
    else:
        tipos = tipo.split()
        ingredientes_filtrados = ingredientes[ingredientes["Tipo"].isin(tipos)]
    
    print(ingredientes_filtrados.to_string())
    return ingredientes_filtrados
    

def cadastrar_ingrediente(ingredientes, tipo ,nome, valor):
    """Cadastra um ingrediente no DataFrame recebido
    
    :param ingredientes: O DataFrame que contém os ingredientes, com colunas Tipo, Nome, Valor
    :type ingredientes: pandas.core.DataFrame
    :param tipo: Tipo do ingrediente, sendo Massa, Molho, Queijo ou Cobertura
    :type tipo: str
    :param nome: Nome do ingrediente
    :type nome: str
    :param valor: Preço do ingrediente
    :type valor: float
    :return: DataFrame atualizado com o ingrediente inserido
    :rtype: pandas.core.DataFrame
    
    >>> df = pd.DataFrame(data=[["Massa", "Tradicional", 5.0]], columns=["Tipo", "Nome", "Valor"])
    >>> cadastrar_ingrediente(df, "Queijo", "Cheddar", 10.0)
         Tipo         Nome Valor
    0   Massa  Tradicional   5.0
    1  Queijo      Cheddar  10.0
    """
    novo_ingrediente = {"Tipo": tipo, "Nome": nome, "Valor": valor}
    ingredientes = pd.concat([ingredientes, pd.DataFrame.from_dict({'Novo': novo_ingrediente}).T], ignore_index=True)
    return ingredientes

def remover_ingrediente(ingredientes, nome_ingrediente):
    """
    Função que remove o ingrediente selecionado por meio do nome

    :param ingredientes: Dataframe contendo as informações de todos os ingredientes
    :type ingredientes: panda.core.Dataframe
    :param nome_ingrediente: Nome do ingrediente a ser removido
    :type nome_ingrediente: str
    :return: Dataframe atualizado, e uma print no console do ingrediente removido
    :rtype: panda.core.Dataframe
    
    >>> df = pd.DataFrame(data=[["Massa", "Tradicional", 5.0], ["Massa", "Fina", 1.0]], columns=["Tipo", "Nome", "Valor"])
    >>> remover_ingrediente(df, "Tradicional")
        Tipo  Nome  Valor
    0  Massa  Fina    1.0
    """
    ingredientes = ingredientes[ingredientes['Nome'] != nome_ingrediente]
    ingredientes.reset_index(drop = True, inplace = True)

    return ingredientes

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
    :param molho: o nome do molho escolhido
    :type molho: str
    :param queijo: o nome do queijo escolhido
    :type queijo: str
    :param cobertura: o nome da cobertura escolhida
    :type cobertura: str
    :rtype: pandas.core.DataFrame

    >>> colunas = ["Tipo", "Nome", "Valor"]
    >>> linhas = [["Massa", "Tradicional", 5.0], ["Massa", "Fina", 5.0],["Molho", "Tomate", 3.50], ["Molho", "Branco", 4.20],["Queijo", "Mussarela", 6.70],["Queijo", "Prato", 8.10],["Cobertura", "Calabresa", 6.30], ["Cobertura", "Lombo", 9.20]]
    >>> ingredientes = pd.DataFrame(data=linhas, columns=colunas)

    >>> montar_pizza(ingredientes=ingredientes, massa="Fina", molho="Branco", queijo="Prato", cobertura="Calabresa")
    Eis a estrutrura da sua pizza:
            Tipo       Nome  Valor
    1      Massa       Fina    5.0
    3      Molho     Branco    4.2
    5     Queijo      Prato    8.1
    6  Cobertura  Calabresa    6.3
    Sua pizza vai custar R$23.6
            Tipo       Nome  Valor
    1      Massa       Fina    5.0
    3      Molho     Branco    4.2
    5     Queijo      Prato    8.1
    6  Cobertura  Calabresa    6.3
    0      PIZZA      TOTAL   23.6

    >>> montar_pizza(ingredientes=ingredientes, massa="Fina", molho="NAOEXISTE", queijo="Prato", cobertura="Calabresa")
    Eis a estrutrura da sua pizza:
            Tipo       Nome  Valor
    1      Massa       Fina    5.0
    5     Queijo      Prato    8.1
    6  Cobertura  Calabresa    6.3
    Sua pizza vai custar R$19.4
            Tipo       Nome  Valor
    1      Massa       Fina    5.0
    5     Queijo      Prato    8.1
    6  Cobertura  Calabresa    6.3
    0      PIZZA      TOTAL   19.4

    >>> montar_pizza(ingredientes=ingredientes, massa="NAOEXISTE", molho="NAOEXISTE", queijo="NAOEXISTE", cobertura="NAOEXISTE")
    Eis a estrutrura da sua pizza:
    Empty DataFrame
    Columns: [Tipo, Nome, Valor]
    Index: []
    Sua pizza vai custar R$0.0
        Tipo   Nome  Valor
    0  PIZZA  TOTAL    0.0
    """

    massa_info = ingredientes[ingredientes["Nome"] == massa]
    molho_info = ingredientes[ingredientes["Nome"] == molho]
    queijo_info = ingredientes[ingredientes["Nome"] == queijo]
    cobertura_info = ingredientes[ingredientes["Nome"] == cobertura]

    pizza = pd.DataFrame([])

    pizza = pd.concat([pizza, massa_info, molho_info, queijo_info, cobertura_info])

    valor_total = pizza["Valor"].sum()
    valor_total = round(valor_total, 2)
    linha_final = pd.DataFrame(data=[["PIZZA", "TOTAL", valor_total]], columns=["Tipo", "Nome", "Valor"])

    print("Eis a estrutrura da sua pizza:", pizza, sep="\n")
    print(f"Sua pizza vai custar R${valor_total}")

    pizza = pd.concat([pizza, linha_final])

    return pizza

if __name__ == "__main__":
    import doctest
    doctest.testmod()
