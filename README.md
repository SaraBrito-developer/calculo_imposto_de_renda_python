Projeto: Simulador de Salário Líquido (IRPF) em Python

Este projeto é um simulador de linha de comando (CLI) que calcula o salário líquido com base nas alíquotas progressivas do Imposto de Renda (IRPF).

O utilizador pode inserir um salário bruto inicial e, em seguida, simular múltiplos aumentos salariais para ver o impacto imediato na alíquota de imposto e no valor líquido recebido.

O código foi refatorado para isolar a lógica de cálculo da interface do utilizador, permitindo a criação de testes unitários robustos.

---

Estrutura do Projeto

O projeto é dividido em dois ficheiros principais:

1.  calculo_salario.py
    * Contém a lógica de negócio CalculoDaAliquota e o programa principal rodar_simulador que lida com a interação do utilizador, tratamento de erros e o loop de simulação.

2.  test_calculo_salario.py
    * Contém a suíte de testes unitários que valida a função CalculoDaAliquota. Os testes verificam todas as faixas de alíquota e os valores-limite, incluindo a correção do "bug do buraco" existente anteriormente no código.

---

Lógica de Negócio (Alíquotas de IR)

A lógica de cálculo de alíquota (simplificada, não considera deduções) segue as seguintes faixas:

* Até R$ 1903.98: 0%
* De R$ 1903.99 até R$ 2826.65: 7.5%
* De R$ 2826.66 até R$ 3751.05: 15%
* De R$ 3751.06 até R$ 4664.68: 22.5%
* Acima de R$ 4664.68: 27.5%

---

Como Usar

1. Executar o Simulador

Para executar o programa e interagir com ele no terminal:

python calculo_salario.py
