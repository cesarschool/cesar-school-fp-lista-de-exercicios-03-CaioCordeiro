# Main file of the Python 3 program.

from questoes import questao_1
from questoes import questao_2
from questoes import questao_3
from questoes import questao_4
from questoes import questao_5

numero_de_questoes = 5

while True:
    try:
        questao = int(input('\nDigite o numero da questao a ser executada (Para sair digite -1): '))
    except ValueError:
        print ("Oops! Esse nao e um numero valido.  Tente novamente...")
        continue

    if questao == -1:
        print("Bye bye!!!")
        break
    elif questao == 1:
        questao_1.main()
    elif questao == 2:
        questao_2.main()
    elif questao == 3:
        questao_3.main()
    elif questao == 4:
        questao_4.main()
    elif questao == 5:
        questao_5.main()
    else:
        print("Questao invalida!!! Digite um valor entre 1 e 5!")
