def CalculoDaAliquota(SalarioBruto):
    if SalarioBruto <= 1903.98:
        return 0
    elif SalarioBruto > 1903.98 and SalarioBruto <= 2826.5:
        return 0.075
    elif SalarioBruto > 2826.65 and SalarioBruto <= 3751.05:
        return 0.15
    elif SalarioBruto > 3751.05 and SalarioBruto <= 4664.68:
        return 0.22
    else:
        return 0.27

SalarioBruto = float(input("digite o valor do seu Salario Bruto: "))

while True:
    Aliquota = CalculoDaAliquota(SalarioBruto)
    print("\nVocê tem uma dedução de: " + str(Aliquota*100))
    SalarioLiquido = SalarioBruto - (SalarioBruto * Aliquota)
    print("\nSeu Salario liquido é de: " + str(SalarioLiquido))
    SalarioBruto += float(input("\ndigite um valor em real de aumento para o seu Salario: "))