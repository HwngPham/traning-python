class Choice:
    ENCRYPT = 'e'
    DECRYPT = 'd'
    TERMINATE = 'q'


class Encryptor:
    def __init__(self, shift_distance=3):
        self.shift_distance = int(shift_distance)

    def encrypt(self, message):
        encrypted_chars = [chr(ord(char) + self.shift_distance)
                           for char in message]
        return ''.join(encrypted_chars).upper()

    def decrypt(self, message):
        decrypted_char = [chr(ord(char) - self.shift_distance)
                          for char in message]
        return ''.join(decrypted_char).upper()


def prompt_action():
    action = input('Do you want to (e)ncrypt or (d)ecrypt or (q)uit ?\n')
    shift_distance = prompt_shift_distance()
    encryptor = Encryptor(shift_distance)

    if action == Choice.TERMINATE:
        return

    if action == Choice.ENCRYPT:
        message = input('Enter message to encrypt.\n')
        encrypted_message = encryptor.encrypt(message)
        print(encrypted_message)

    if action == Choice.DECRYPT:
        message = input('Enter message to decrypt.\n')
        encrypted_message = encryptor.decrypt(message)
        print(encrypted_message)

    return prompt_action()


def prompt_shift_distance():
    user_input = input('Please enter the key (0 to 25) to use.\n')
    is_valid_input = user_input.isdecimal() and 0 <= int(user_input) <= 25
    return user_input if is_valid_input else prompt_shift_distance()


if __name__ == '__main__':
    prompt_action()
