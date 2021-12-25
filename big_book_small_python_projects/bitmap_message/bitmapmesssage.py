bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
....................................................................
"""


class BitmapDrawer:
    def __init__(self):
        self.message = ''
        self.characters_stack = []

    def execute(self):
        user_input = input('Enter the message to display with the bitmap.\n')
        if not user_input:
            return self.execute()

        self.message = user_input
        print(self.__transform_bitmap())

    def __populate_characters_stack(self):
        if len(self.characters_stack) > 0:
            return
        self.characters_stack = list(self.message)
        self.characters_stack.reverse()

    def __transform_bitmap(self):
        result = []

        for bit in bitmap:
            self.__populate_characters_stack()

            translated_character = bit if bit in [' ', '\n'] \
                else self.characters_stack.pop()
            result.append(translated_character)

        return ''.join(result)


if __name__ == '__main__':
    BitmapDrawer().execute()
