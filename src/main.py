from core import Menu

if __name__ == "__main__":
    result = ""
    while True:
        menu = Menu()
        menu.create(result)
        result = ""
        option = menu.get_option()
        result = menu.select_option(option)

        if option == "99":
            break
