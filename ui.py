from models import short_handler


def user_interface():
    url = input("Please enter your url: ")
    print(url)
    user = short_handler.ReplaceUrl()
    print(user.convert_long_to_short(url))
    print(user.convert_short_to_long("tt"))
    print(user.convert_short_to_long("http://uRshort.us/k"))
    print(user.convert_short_to_long('http://www.uRshort.us/a'))
    print(user.convert_short_to_long("a"))


if __name__ == '__main__':
    user_interface()
