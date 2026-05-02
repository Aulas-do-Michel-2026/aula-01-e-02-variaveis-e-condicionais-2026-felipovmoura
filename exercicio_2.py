"""
#### Exercício 2

Uma fórmula recomenda 2mg de medicamento por kg de peso do paciente.

Peça o peso de uma pessoa e calcule a dose recomendada.

Exemplo:

Digite o peso do paciente (em kg):
70

Resposta:
Média: 140 mg
"""
peso = float(input("Digite o peso do paciente (em kg): "))
dose_recomentada = peso * 2

print(f"A dose recomendada é {dose_recomentada:.2f}", "mg")
