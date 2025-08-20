from datetime import datetime
def days_alive(date):
    date_time = datetime.strptime(date, '%d/%m/%Y')
    now = datetime.now()
    dias = (now - date_time).days
    return dias
    
data = input("Digite sua data de nascimento (dd/mm/aaaa): ")
print(f"Você está vivo a {days_alive(data)} dias!")