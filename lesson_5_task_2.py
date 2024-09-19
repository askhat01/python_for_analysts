print('\nЗадача_2')
names = ['Askhat', 'Max', "Olya"]
salaries = [16000, 30000, 26000]
awards = ['11.0%', '8.25%', '9%']
print(f'исходные данные:\n{names}\n{salaries}\n{awards}')
print('Решение:')

print({name: salary * float(award[:-1]) / 100 for name, salary, award in zip(names, salaries, awards)})