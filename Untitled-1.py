def switch_dia(dia):
    dias = {
1: "Segunda-feira",
2: "Terça-feira",
3: "Quarta-feira",
4: "quinta-feira",
5: "sexta-feira",
6: "sábado",
7: "domingo",
}
    return dias.get(dia, "Dia inválido")
dia_selecionado =switch_dia(int(input("digite o s dia: ")))
print("O dia é:", dia_selecionado)
