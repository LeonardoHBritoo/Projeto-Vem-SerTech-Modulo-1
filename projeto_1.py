#Lista de restaurantes previamente cadastrados
restaurantes_cadastrados = [['Madeiro', [['Lasagna', 32.8, '45'], ['X-Burguer', 23.6, '20'], ['Feijão Tropeiro', 23.9, '20'], ['Ceviche', 99.98, '45']]], ['Mcdonalds', [['Batata Frita', 40.0, '20'], ['Macfeliz', 12.0, '23']]], ['Fornalha', [['Leitão À Pururuca', 53.44, '45'], ['Arroz Carreteiro', 35.8, '20']]], ['Aleluia', [['Fusilli À Carbonara', 33.9, '30']]], ['Vila Comini', [['Lasagna De Espinafre', 22.6, '67']]], ['Casa De Pedra', [['Costela Na Brasa', 77.98, '24']]], ['Alfaro', [['Lombo Assado', 32.6, '23,4']]]]

#Exibe o menu aos usuãrios 

def menu():
    menu = '''
  ---------- Menu ----------
  [1] - Adicionar Restaurante
  [2] - Realizar Pedido
  [3] - Adicionar Pratos à um Restaurante
  [4] - Visualizar Cardápios
  [0] - Finalizar
  --------------------
  => '''
    return input(menu)
  
#Função responsável por adicionar pratos ao cardápio de um restaurante cadastrado - não permitindo adicionar prato repetido. 
# A função retorna uma lista contendo nome, valor e tempo de preparo do prato

def adicionar_pratos(restaurante_selecionado):
  nome_prato = input('Nome do prato: ').title()
  prato_repetido = testar_existencia_cardapio(nome_prato, restaurante_selecionado)
  if prato_repetido:
    pass
  else:
    valor_prato_str = input('Valor do prato: ').replace(',', '.')
    valor_prato = float(valor_prato_str)
    tempo_preparo = input('Tempo de preparo: ')

    return [nome_prato, valor_prato, tempo_preparo]
  
#Função responsável por adicionr cardápio ao restaurante previamente cadastrado.
#A função retorna o cardapio atualizado.

def adicionar_cardapio(restaurante):
  cardapio = []
  atualizar_cardapio = True
  while atualizar_cardapio:
    prato_adicionado = adicionar_pratos(restaurante)
    if prato_adicionado != None:
      cardapio.append(prato_adicionado)
    else:
      print(f'\nEsse prato já existe')
    print('[0] - Finalizar \n[1] - Continuar')
    if input() == '0':
        break
  return cardapio

#Funcão responsável por solicitar cadastro de restaurante ao usuário, possibilitando o cadastro do cardápio em seguida. 
# Com isso, cria-se uma lista com os restaurantes e seus respctivos cardápios.

def adicionar_restaurante(nome_restaurante):
  print('Adicione ao menos um prato ao cardápio para confirmar cadastro:\n')
  cardapio_restaurante = adicionar_cardapio(restaurantes_cadastrados[-1])
  novo_restaurante = [nome_restaurante,cardapio_restaurante]
  restaurantes_cadastrados.append(novo_restaurante)

#Função responsável por testar se o restaurante já foi cadastrado. 
# Para tanto, utilizou-se da função index com a finalidade de encontrar a posição do restaurante buscado. 
#A função retona a  posição por meio da variável código. 

def testar_existencia_restaurante(restaurante_buscado):
  for restaurante in restaurantes_cadastrados:
      if restaurante_buscado == restaurante[0]:
        codigo = restaurantes_cadastrados.index(restaurante)
        return codigo
  return None

#Função responsavel por verificar se um prato está presente no cardápio do restaurante selecionado
#A função retorna falso se o prato não for encontrado após iteração completa.

def testar_existencia_cardapio(prato_buscado, restaurante_selecionado):
  for prato in restaurante_selecionado[1]:
    if prato_buscado == prato[0]:
      return True 
  return False

#Função responsável por pedir ao usuário o nome de um restaurante e verifica sua existencia.
#Caso não exista, pede ao usuario confirmação para adicionar.

def novo_restaurante():
  restaurante_buscado = input('Nome do restaurante: ').title()
  busca_restaurante = testar_existencia_restaurante(restaurante_buscado)
  if busca_restaurante == None:
    print(f"Confirmar nome do restaurante: {restaurante_buscado} ? [1] - Sim [0] - Não")
    confirmacao = int(input())
    if confirmacao:
      return adicionar_restaurante(restaurante_buscado)
  else:
    print(f'\nEsse restaurante já está cadastrado')
    
#Função responsável por mostrar informações sobre o pedido - listando pratos, preços, tempo de preparo e quantidade de itens.
#Ela exibe ao usuário os detalhes formatados
  
def exibir_pedido(pedido, qnt_pedido):
  print('Nº |     Prato       |      Preço       | Tempo de Preparo  | Quantidade | ')
  for i in pedido:
      print(f'{pedido.index(i):02d} | {i[0]:^15} | {(i[1] * qnt_pedido[pedido.index(i)]):^16} | {i[2]:^17} | {qnt_pedido[pedido.index(i)]:^11}|')

#Função responsável por exibir lista de restaurantes cadastrados.
#Se nenhum restaurante estiver cadastrado, informa ao usuário.

def exibir_restaurante():
  if len(restaurantes_cadastrados) == 0:
        print("Nenhum restaurante cadastrado!")
        return
  print('Estes são os restaurantes_cadastrados disponíveis:')
  for i in range(len(restaurantes_cadastrados)):
    print(i + 1,'-',restaurantes_cadastrados[i][0])
    


def novo_pedido():
  exibir_restaurante()
  restaurante = int(input('Insira o número: '))

  # Validação que evita do usuário fornecer valores fora da lista de restaurantes_cadastrados
  while restaurante not in range(1,len(restaurantes_cadastrados)+1):
    print('Restaurante não encontrado!')
    exibir_restaurante()
    restaurante = int(input('Insira o número: '))

  for i in range(1,len(restaurantes_cadastrados)+1):
    if i == restaurante:
      return (i - 1)

def exibir_cardapio():
  restaurante = novo_pedido()
  print(f'            Cardápio do Restaurante {restaurantes_cadastrados[restaurante][0]}\n')
  print('| ID |      Prato      |      Preço       | Tempo de Preparo  |')
  print('-'*63)
  pratos = restaurantes_cadastrados[restaurante][1]
  for prato in pratos:
    print(f'|{pratos.index(prato):^3} |{prato[0]:^16} | {prato[1]:^16} | {prato[2]:^17} |')
    print('-'*63)
  return pratos

def realizar_pedido():
  pratos = exibir_cardapio()
  qnt_do_pedido = []
  pedidos = []
  while True:
    prato_desejado = int(input('Digite o prato ID do prato: '))
    qnt_do_pedido.append(int(input(f'Qual a quantidade? ')))
    for prato in pratos:
      if prato_desejado == pratos.index(prato):
        pedidos.append(prato)
    print('[1] - Continuar com pedido \n[0] - Finalizar pedido')
    if input() == '0':
      break
  exibir_pedido(pedidos, qnt_do_pedido)

def adicionar_novo_pratos():
  id = novo_pedido()
  print("Adicione um novo prato ao cardápio:")
  cardapio_adicional = adicionar_pratos(restaurantes_cadastrados[id])
  if cardapio_adicional != None:
    restaurantes_cadastrados[id][1].append(cardapio_adicional)
    print("Cardápio atualizado!")
  else:
      print(f'\nEsse prato já existe')

def main():
  while True:
    opcao = menu()
    if opcao == '1': #Adicionar Restaurante
      novo_restaurante()
    elif opcao == '2': #Realizar Pedido
      realizar_pedido()
    elif opcao == '3': #Adicionar Pratos à um Restaurante
      adicionar_novo_pratos()
    elif opcao == '4': #Visualizar Cardápios
      exibir_cardapio()
    elif opcao == '0':
      print('Encerrando...')
      break
    else:
      print('Opção Inválida')
  
main()