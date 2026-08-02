while True:
    user_word = input('Введіть слово, у якому є літера "h": ')

    if "h" in user_word.lower():
        print('Дякую, у введеному слові є літера "h".')
        break

    print('У цьому слові немає літери "h". Спробуйте ще раз!')