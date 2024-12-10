# todo: Взлом шифра

"""
Вы знаете, что фраза зашифрована кодом Цезаря с неизвестным сдвигом.
Попробуйте все возможные сдвиги и расшифруйте фразу.

grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.

"""

alphabet = 'abcdefghijklmnopqrstuvwxyz'
message = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."
key = ''

for key in range(0,26):
    decoding = ''
    for i in message:
        if i in alphabet:
            position = alphabet.find(i) # Нашли индекс буковки из сообщения для алфавита
            enc_position = (position - key) % 26 # Меняем индекс на нужный нам сдвиг по алфавиту, % 26 прокручивает нас к началу
            decoding += alphabet[enc_position] # Записываем в decoding буковки с новыми позициями в алфавите
        else:
            decoding += i
    print(f'Cдвиг: {key}, расшифровка: {decoding}')


'''Cдвиг: 6, расшифровка: although that way may not be obvious at first unless you're dutch.'''

