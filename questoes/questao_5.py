## QUESTÃO 5 ##
#
# Crie uma implementação da cifra rotacional, às vezes também chamada de cifra de César.
# 
# A cifra de César é uma simples cifra de deslocamento que se baseia na transposição 
# de todas as letras do alfabeto usando uma chave inteira entre 0 e 26. 
# O uso da chave 0 ou 26 sempre produzirá a mesma saída devido à aritmética modular. 
# A letra é deslocada para tantos valores quanto o valor da chave.
#
# A notação geral para cifras rotacionais é ROT + <chave>. A cifra rotacional mais comumente usada é a ROT13.
#
# Um ROT13 no alfabeto latino seria o seguinte:
# 	Normal:  abcdefghijklmnopqrstuvwxyz
#	Cifrado: nopqrstuvwxyzabcdefghijklm
#
# Exemplos:
#	Entrada: ROT5 omg 
#          Saída: trl
#	Entrada: ROT0 c 
#          Saída: c
#	Entrada: ROT26 Cool 
#          Saída: Cool
#	Entrada: ROT13 The quick brown fox jumps over the lazy dog. 
#          Saída: Gur dhvpx oebja sbk whzcf bire gur ynml qbt.
#	Entrada: ROT13 Gur dhvpx oebja sbk whzcf bire gur ynml qbt. 
#          Saída: The quick brown fox jumps over the lazy dog.
#
# Se um valor de entrada inválido for digitado, a seguinte mensagem 
# deve ser impressa: 'Erro'. 
# Entradas inválidas podem ser entradas que contém códigos de rotações 
# inválidos ou mensagens contendo caracteres que não estão no alfabeto. 
# Exemplos:
# 	Entrada: RARA abc Saída: Erro
# 	Entrada: ROT5 c99 Saída: Erro
#
# As entradas devem ser sempre compostas por ROT + <chave> + ' ' + 'mensagem', 
# ou seja, a cifra rotacional e a mensagem a ser cifrada separados por vírgula.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    MAX_KEY_SIZE = 26
    def getTranslatedMessage(message, key):



         translated = ''



         for symbol in message:

             if symbol.isalpha():

                 num = ord(symbol)

                 num += key



                 if symbol.isupper():

                     if num > ord('Z'):

                         num -= 26

                     elif num < ord('A'):

                         num += 26

                 elif symbol.islower():

                     if num > ord('z'):

                         num -= 26

                     elif num < ord('a'):

                         num += 26



                 translated += chr(num)

             else:

                 translated += symbol

         return translated



    flag = 0
    keyinput = input('')
    rot = keyinput.split(' ',1)
    keys = rot[0].split('ROT',1)
    if keys[0] != '':
        print('Error')

    else:
        key0 = keys[1]
        ms = rot[1]
        for i in rot[1]:
            if i.isnumeric() == True:
                flag = 1
            else:
                continue
        if (key0.isnumeric() == False) or (int(key0) < 0 or int(key0) > MAX_KEY_SIZE)or(flag == 1):
            print('Error')


        else:
            key =int(key0)
            print(getTranslatedMessage(ms, key)) 

    





    
if __name__ == '__main__':
    main()
