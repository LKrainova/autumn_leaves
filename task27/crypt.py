def cezary():

    message = input("Enter the message you'd like to encode: \n")
    key = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
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

if __name__ == '__main__':
    cezary()

