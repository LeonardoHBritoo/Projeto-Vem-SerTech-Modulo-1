restaurantes = [['Madeiro', [['Lasagna', 32.8, '45'], ['X-Burguer', 23.6, '20'], ['Feijão Tropeiro', 23.9, '20'], ['Ceviche', 99.98, '45']]], ['Mcdonalds', [['Batata Frita', 40.0, '20'], ['Macfeliz', 12.0, '23']]], ['Fornalha', [['Leitão À Pururuca', 53.44, '45'], ['Arroz Carreteiro', 35.8, '20']]], ['Aleluia', [['Fusilli À Carbonara', 33.9, '30']]], ['Vila Comini', [['Lasagna De Espinafre', 22.6, '67']]], ['Casa De Pedra', [['Costela Na Brasa', 77.98, '24']]], ['Alfaro', [['Lombo Assado', 32.6, '23,4']]]]

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

def adicionar_pratos():
  nome_prato = input('Nome do prato: ').title()
  valor_prato_str = input('Valor do prato: ').replace(',', '.')
  valor_prato = float(valor_prato_str)
  tempo_preparo = input('Tempo de preparo: ')

  return [nome_prato, valor_prato, tempo_preparo]

def adicionar_cardapio():
  cardapio = []
  finaliza = True
  while finaliza:
    prato_adicionado = adicionar_pratos()
    cardapio.append(prato_adicionado)
    print('[0] - Finalizar \n[1] - Continuar')
    if input() == '0':
        break
  return cardapio

def adicionar_restaurante(nome_restaurante):
  nome_restaurante1 = nome_restaurante
  cardapio_restaurante = adicionar_cardapio()
  novo_restaurante = [nome_restaurante1,cardapio_restaurante]
  restaurantes.append(novo_restaurante)

def testar_existencia_restaurante(restaurante_buscado):
  for restaurante in restaurantes:
      if restaurante_buscado == restaurante[0]:
        codigo = restaurantes.index(restaurante)
        return codigo
  return None

def novo_restaurante():
  restaurante_buscado = input('Nome do restaurante: ').title()
  busca_restaurante = testar_existencia_restaurante(restaurante_buscado)
  if busca_restaurante == None:
    print("Restaurante não encontrado. Deseja Adicionar [1] - Sim [0] - Não")
    x = int(input())
    if x:
      return adicionar_restaurante(restaurante_buscado)
  else:
    return busca_restaurante
  
def exibir_pedido(pedido):
  ordem = sorted(pedido)
  tem = []
  print('Nº |     Prato       |      Preço       | Tempo de Preparo  | Quantidade | ')
  for i in ordem:
    qnt = ordem.count(i)
    if i not in tem:
      print(f'{pedido.index(i):02d} | {i[0]:^15} | {(i[1] * qnt):^16} | {i[2]:^17} | {qnt:^11}|')
      tem.append(i)
    else:
      continue

def exibir_restaurante():
  if len(restaurantes) == 0:
        print("Nenhum restaurante cadastrado!")
        return
  print('Estes são os restaurantes disponíveis:')
  for i in range(len(restaurantes)):
    print(i + 1,'-',restaurantes[i][0])

def novo_pedido():
  print('De qual restaurante gostaria de pedir?')
  exibir_restaurante()
  restaurante = int(input('Insira o número: '))
  for i in range(len(restaurantes)):
    if i == restaurante:
      return i - 1

def exibir_cardapio():
  restaurante = novo_pedido()
  print(f'            Cardápio do Restaurante {restaurantes[restaurante][0]}\n')
  print('|     Prato       |      Preço       | Tempo de Preparo  |')
  print('-'*58)
  pratos = restaurantes[restaurante][1]
  for prato in pratos:
    print(f'|{prato[0]:^16} | {prato[1]:^16} | {prato[2]:^18} |')
    print('-'*58)

def realizar_pedido():
  exibir_cardapio()
  pedidos = []
  while True:
    prato_desejado = input('Digite o prato desejado: ').title()
    for restaurante in restaurantes:
      cardapio = restaurante[1]
      for prato in cardapio:
        if prato_desejado == prato[0]:
          pedidos.append(prato)
    print('[1] - Continuar com pedido \n[0] - Finalizar pedido')
    if input() == '0':
      break
  exibir_pedido(pedidos)

def adicionar_novo_pratos():
  exibir_restaurante()
  
  teste = novo_restaurante()
  print("Adicione um novo prato ao cardápio:")
  cardapio_adicional = adicionar_pratos()
  restaurantes[teste][1].append(cardapio_adicional)
  print("Cardápio atualizado!")

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
      ('Opção Inválida')
  
main()