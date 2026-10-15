from colorama import Fore, Style

niveis = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]

def definir_cor(nivel):
    if nivel == "Muito baixo (crítico)":
        return Fore.RED
    elif nivel == "Baixo":
        return Fore.YELLOW
    elif nivel == "Médio":
        return Fore.GREEN
    elif nivel == "Alto":
        return Fore.CYAN
    elif nivel == "Muito alto (alerta)":
        return Fore.BLUE


print("Situação do nível do reservatório de água\n")

for numero in range(1, 6):
    situacao = niveis[numero - 1]
    cor = definir_cor(situacao)
    print(cor + f"Nível {numero}: {situacao}")
    print(Style.RESET_ALL)