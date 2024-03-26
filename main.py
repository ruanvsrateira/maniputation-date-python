from datetime import date, datetime

months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
today = date.today()
birthday = date(2004, 7, 29)

#Obtendo informações do dia de hoje
print(f"Hoje é Dia {today.day} de {months[today.month-1]} de {today.year}")

#Obtendo minha data de nascimento, através da instância birthday
print(f"Eu Nasci no dia {birthday.day} de {months[birthday.month-1]} de {birthday.year}")

'''
Formatando data em d/m/a h:m:s 
%d = day
%m = month
%Y = year
%H = hour
%M = minutes
%S = seconds
'''
formated_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
print(f"Data formatada de hoje: {formated_date}")

