restaurantes = []

def menu():
    menu = '''
  ---------- Menu ----------
  [1] - Adicionar Restaurante
  [2] - Realizar Pedido
  [0] - Finalizar
  --------------------
  => '''
    return input(menu)

def adiciona_cardapio():
  cardapio = []
  finaliza = True
  while finaliza:
    prato = input('Nome do prato: ')
    valor_prato_str = input('Valor do prato: ')
    valor_prato_str = valor_prato_str.replace(',', '.')
    valor_prato = float(valor_prato_str)
    tempo_preparo = input('Tempo de preparo: ')
    print('[0] - Finalizar \n[1] - Continuar')
    finalizar = input()
    finaliza = finalizar != '0'
    pratos = []
    pratos.append(prato)
    pratos.append(valor_prato)
    pratos.append(tempo_preparo)
    cardapio.append(pratos) 
  return cardapio

def adiciona_restaurante():
  restaurante = input('Nome do restaurante: ')
  cardapio = adiciona_cardapio()
  restaurante_atual = []
  restaurante_atual.append(restaurante)
  restaurante_atual.append(cardapio)
  restaurantes.append(restaurante_atual)

def exibe_menu(nome_restaurante):
  for item in restaurantes:
    if nome_restaurante == item[0]:
      print(f'            Cardápio do Restaurante {item[0]}\n')
      print('|     Prato       |      Preço       | Tempor de Preparo  |')
      print('-'*58)
      prato = item[1]
      for p in prato:
        print(f'|{p[0]:^16} | {p[1]:^16} | {p[2]:^18} |')
        print('-'*58)

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

def realizar_pedido():
  pedidos = []
  sem_ideia = 1
  while sem_ideia:
    pedido = input('Digite o prato que desejado: ').title()
    for item in restaurantes:
      prato = item[1]
      for p in prato:
        if pedido in p:
          pedidos.append(p)
    print('[1] - Continuar com pedido \n[0] - Finalizar pedido')
    continua_pedido = input()
    if continua_pedido == "0":
      sem_ideia = 0
  exibir_pedido(pedidos)

def selecionar_restaurante():
  print('Estes são os restaurantes disponíveis:')
  for restaurante in restaurantes:
      print(restaurante[0])

  resto = 1
  while resto:
    restaurante_buscado = input('Digite o nome do restaurante: ').title()
    for i in restaurantes:
      if restaurante_buscado in i:
        exibe_menu(restaurante_buscado)
        resto = 0
  realizar_pedido()

def main():
  while True:
    opcao = menu()
    if opcao == '1':
      adiciona_restaurante()
    elif opcao == '2':
      selecionar_restaurante()
    elif opcao == '0':
      print('Encerrando...')
      break
    else:
      ('Opção Inválida')

main()