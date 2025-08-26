
funcionarios = set(['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa'])
turno_dia = set(['Ana', 'Marcos', 'Alice', 'Melissa'])
turno_noite = set(['Pedro', 'Sophia', 'Bruno'])
tem_carro = set(['Marcos', 'Alice', 'Bruno', 'Melissa'])


# têm carro e trabalham à noite
print(f'têm carro e trabalham à noite: {tem_carro & turno_noite} \n')
#têm carro e trabalham durante o dia
print(f'têm carro e trabalham o dia: {tem_carro & turno_dia} \n')
# não têm carro 
print(f'não têm carro : {funcionarios - tem_carro} \n')
