import pandas as pd
import random

# definindo o numero de clientes
n_clientes = 100

# criando funções para gerar valores aleatórios
def gerar_score():
    return random.randint(300, 850)

def gerar_renda():
    return random.randint(1200, 20000)

def gerar_endividamento():
    return round(random.uniform(0, 1), 2)

def gerar_risco(score, endividamento):
    if score > 700 and endividamento < 0.3:
        return "Baixo"
    elif score > 500:
        return "Médio"
    else:
        return "Alto"

def gerar_recomendacao(risco):
    if risco == "Baixo":
        return random.choice(['Cartão de Crédito', 'Investimentos'])
    elif risco == "Médio":
        return random.choice(["Empréstimo Pessoal", "Refinanciamento"])
    else:
        return "Educação Financeira"

# formatando dataset
data = {
    "ID": [random.randint(0, 200) for _ in range(n_clientes)],
    "Idade": [random.randint(18, 70) for _ in range(n_clientes)],
    "Renda_Mensal": [gerar_renda() for _ in range(n_clientes)],
    "Estado_Civil": [random.choice(["Solteiro", "Casado", "Divorciado", "Viúvo"]) for _ in range(n_clientes)],
    "Score_Credito": [gerar_score() for _ in range(n_clientes)],
    "Endividamento": [gerar_endividamento() for _ in range(n_clientes)],
}

# Aicionando colunas extras
data["Risco_Credito"] = [gerar_risco(score, endiv) for score, endiv in zip(data["Score_Credito"], data["Endividamento"])]
data["Recomendacao_Produto"] = [gerar_recomendacao(risco) for risco in data["Risco_Credito"]]

df = pd.DataFrame(data)

# salvando em arquivo csv
df.to_csv("score_credito.csv", index=False)

'''se der certo o código vou gerar uma mensagem que deu certo 100%'''

print ("arquivo gerado")