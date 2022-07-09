from datetime import date, time, datetime, timedelta

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y %H: %M: %S '))
    print(data_atual.strftime('%c'))
    print(data_atual.weekday())
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabádo', 'Domingo')
    print(tupla[data_atual.weekday()])
    print(data_atual.month)
    tupla_mes =('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
    print(tupla_mes[data_atual.month])
    data_criada = datetime(2012, 12, 12, 16, 30, 10)
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_string = '01/10/2014 18:55:10'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    nova_data = data_convertida - timedelta (days=304, hours=8, minutes=50, seconds=10)
    print(nova_data)


def trabalhando_com_data():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%d %m %Y')
    print(data_atual_str)

def trabalhando_com_temi():
    horario = time(hour=15, minute=18, second=30)
    horario_str = horario.strftime('%H: %M: %S')
    print(horario_str)
    print(type(horario.strftime))

if __name__ == '__main__':
    # trabalhando_com_data()
    # trabalhando_com_temi()
    trabalhando_com_datetime()