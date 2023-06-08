# Cria duas listas representando os calendários para anos normais e bissextos
normal_year = [[day for day in range(0, 31)],
              [day for day in range(0, 28)],
              [day for day in range(0, 31)],
              [day for day in range(0, 30)],
              [day for day in range(0, 31)],
              [day for day in range(0, 30)],
              [day for day in range(0, 31)],
              [day for day in range(0, 31)],
              [day for day in range(0, 30)],
              [day for day in range(0, 31)],
              [day for day in range(0, 30)],
              [day for day in range(0, 31)]]

leap_year =  [[day for day in range(0, 31)],
              [day for day in range(0, 29)],
              [day for day in range(0, 31)],
              [day for day in range(0, 30)],
              [day for day in range(0, 31)],
              [day for day in range(0, 30)],
              [day for day in range(0, 31)],
              [day for day in range(0, 31)],
              [day for day in range(0, 30)],
              [day for day in range(0, 31)],
              [day for day in range(0, 30)],
              [day for day in range(0, 31)]]


def time_machine(year_destiny):
  # Lida com caso do ano de transição de calendário 1918
  if year_destiny == 1918:
    count = 0
    # Exclui o 1º mês e começa a partir de Fevereiro
    for month in range(1, len(normal_year)+1):
      if month == 1:
        # Percorre o mês de fevereiro a partir do dia 14
        for day in range(14, 29):
          count += 1
      # Percorre os demais meses normalmente
      for day in range(0, len(normal_year[month])):
        count += 1
        # Quando chega na data desejada, retorna a data formatada
        if count == 253:
          return str(normal_year[month][day+1]) + '/' + str(month+1) + '/' + str(year_destiny)
  
  # Lida com o caso de anos no calendário juliano
  elif 1700 <= year_destiny <= 1917:
    count = 0
    # Identifica se o ano é bissexto
    if year_destiny % 4 == 0:
      # Percorre o ano e conta os dias
      for month in range(0, len(leap_year)):
        for day in range(0, len(leap_year[month])):
          count += 1
          # Retorna o 256º dia do dado ano
          if count == 256:
            return str(leap_year[month][day+1]) + '/' + str(month+1) + '/' + str(year_destiny)
    # Ano que NÃO é bissexto
    else:
      for month in range(0, len(normal_year)):
        for day in range(0, len(normal_year[month])):
          count += 1
          if count == 256:
            return str(normal_year[month][day+1]) + '/' + str(month+1) + '/' + str(year_destiny)

  # Lida com o caso de anos no calendário gregoriano
  elif 1919 <= year_destiny <= 2700:
    count = 0
    # Identifica se o ano é bissexto
    if year_destiny % 4 == 0 and year_destiny % 100 !=0 or year_destiny % 400 == 0:
      # Percorre o ano e conta os dias
      for month in range(0, len(leap_year)):
        for day in range(0, len(leap_year[month])):
          count += 1
          # Retorna o 256º dia do dado ano
          if count == 256:
            return str(leap_year[month][day+1]) + '/' + str(month+1) + '/' + str(year_destiny)
    # Ano que NÃO é bissexto
    else:
      for month in range(0, len(normal_year)):
        for day in range(0, len(normal_year[month])):
          count += 1
          if count == 256:
            return str(normal_year[month][day+1]) + '/' + str(month+1) + '/' + str(year_destiny)
  
  else:
    return print('Cannot travel past year 2700')
