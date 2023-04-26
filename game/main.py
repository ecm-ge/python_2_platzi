#Juego de Piedra, Papel o Tijera
import random

win_user = 0
win_pc = 0

while win_user != 3 and win_pc !=3:
    user_option = str(input('Seleccione, piedra, papel o tijera: '))
    user_option = user_option.lower()
    computer_option = random.randint(1, 3)
    if computer_option == 1:
        computer_option = 'piedra'
    elif computer_option == 2:
        computer_option = 'papel'
    elif computer_option == 3:
        computer_option = 'tijera'

    if user_option == computer_option:
        print("Usuario eligio {} y PC eligio {} asi que el resultado es: ".format(user_option, computer_option))
        print('EMPATE!!!')
    elif (user_option == 'piedra' and computer_option == 'papel') or (
            user_option == 'papel' and computer_option == 'tijera') or \
            (user_option == 'tijera' and computer_option == 'piedra'):
        print("Usuario eligio {} y PC eligio {} asi que el resultado es: ".format(user_option, computer_option))
        print('PC Gana!!!')
        win_pc+=1
    elif (user_option == 'piedra' and computer_option == 'tijera') or (
            user_option == 'papel' and computer_option == 'piedra') or \
            (user_option == 'tijera' and computer_option == 'papel'):
        print("Usuario eligio {} y PC eligio {} asi que el resultado es: ".format(user_option, computer_option))
        print('Usuario Gana!!!')
        win_user+=1
    else:
        print('Opcion Erronea')

    print('El marcador va Usuario: {} vs PC: {}'.format(win_user, win_pc))

if win_pc == 3:
    print('PC GANA EL JUEGO')
elif win_user ==3:
    print('USER GANA EL JUEGO')