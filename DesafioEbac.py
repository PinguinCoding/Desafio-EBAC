from datetime import datetime, timedelta


def maquina_do_tempo(ano_destino):
    try:
        if ano_destino == 1918:
            data = datetime(ano_destino, 1, 1) + timedelta(days=268)
            return data.strftime("%d/%m/%Y")

        elif 1917 >= ano_destino >= 1700:
            if ano_destino % 4 == 0:
                data = datetime(ano_destino, 1, 1) + timedelta(days=254)
                return data.strftime("%d/%m/%Y")

            else:
                data = datetime(ano_destino, 1, 1) + timedelta(days=255)
                return data.strftime("%d/%m/%Y")

        elif 2700 >= ano_destino >= 1919:
            data = datetime(ano_destino, 1, 1) + timedelta(days=255)
            return data.strftime("%d/%m/%Y")

        else:
            return print('Não é possível viajar para esse ano!')

    except ValueError:
        return print(f'{ano_destino} não é um valor válido para a viagem!')

    except TypeError:
        return print(f'{ano_destino} não é um tipo de entrada válido para a viagem!')

    except Exception as exc:
        raise exc

y = int(input('Input: '))
print(f'Output: {maquina_do_tempo(y)}')