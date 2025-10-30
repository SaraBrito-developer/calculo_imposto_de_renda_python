# -*- coding: utf-8 -*-

def CalculoDaAliquota(SalarioBruto):
    """
    Calcula a alíquota de imposto com base no salário bruto.
    """
    if SalarioBruto <= 1903.98:
        return 0.0
    elif SalarioBruto <= 2826.65: 
        return 0.075
    elif SalarioBruto <= 3751.05:
        return 0.15
    elif SalarioBruto <= 4664.68:
        return 0.225 
    else:
        return 0.275

def calcular_e_mostrar_salario(SalarioBruto):
    """
    Função auxiliar para calcular e imprimir os detalhes do salário.
    Usa f-strings para uma formatação mais limpa.
    """
    Aliquota = CalculoDaAliquota(SalarioBruto)
    SalarioLiquido = SalarioBruto - (SalarioBruto * Aliquota)
    
    print(f"\nSalário Bruto: R$ {SalarioBruto:.2f}")
    print(f"Alíquota de Imposto: {Aliquota*100:.1f}%")
    print(f"Salário Líquido: R$ {SalarioLiquido:.2f}")

def rodar_simulador():
    try:
        # Pede o salário inicial
        SalarioBruto = float(input("Digite o valor do seu Salário Bruto: "))
        calcular_e_mostrar_salario(SalarioBruto)
        
        while True:
            aumento_str = input("\nDigite um valor de aumento (ou 's' para sair): ")
            
            if aumento_str.lower() == 's':
                print("Saindo do simulador. Até logo!")
                break
                
            try:
                aumento = float(aumento_str)
                if aumento < 0:
                    print("Por favor, digite um valor de aumento positivo.")
                    continue
                    
                SalarioBruto += aumento
                calcular_e_mostrar_salario(SalarioBruto)
                
            except ValueError:
                print("Entrada inválida. Por favor, digite um número ou 's'.")

    except ValueError:
        print("Erro: Você deve digitar um número válido para o salário inicial.")

if __name__ == "__main__":
    rodar_simulador()
