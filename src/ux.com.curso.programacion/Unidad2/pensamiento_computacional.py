total_acumulado = 0
semanas = 0
meta = 2500

while total_acumulado < meta:
    salario_semanal = float(input("Ingrese el salario semanal: "))
    
    total_acumulado = total_acumulado + salario_semanal
    
    semanas = semanas + 1

print("Semanas trabajadas:", semanas)
