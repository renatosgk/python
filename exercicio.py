#exercicio para sexta-feira " pegar os campos month e day da data atual
# perguntar o dia e mes do nascimento do usuário
# descobrir se a pessoa ja fez aniversario esse ano e printar uma mensagem de acordo ."
import datetime
data=datetime.datetime.now()

ano=data.year
mes=data.month
dia=data.day

dia_usuario=int(input("qual o dia do seu aniversário:"))
mes_usuario=int(input("qual o mes do seu aniversário:"))
ano_usuario=int(input("qual o ano do seu aniversário:"))

idade_usuario=(ano - ano_usuario)

print(f"seu aniversario é no dia {dia_usuario}/{mes_usuario}/{ano_usuario}")


if dia_usuario <= dia and mes_usuario <=mes:
    print(f"parabens voce fez aniversario esse ano! e tem {idade_usuario} ")
else:
    print(f"voce ainda nao fez aniversario essse ano , e vai fazer {idade_usuario}")




