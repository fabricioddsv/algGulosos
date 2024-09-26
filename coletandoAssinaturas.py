n = int(input())
horarios = sorted([list(map(int, input().split())) for i in range(n)], key=lambda x: x[1])
print(horarios)
horas_dia = 24

contador = 1
compare = horarios[0][1]
horarios_visitados = [compare]

for i in range(1, len(horarios)):
    if horarios[i][0] > compare:
        contador += 1
        compare = horarios[i][1]
        horarios_visitados.append(compare)

print(contador)
print(f"{horarios_visitados[0]} {horarios_visitados[1]}")
