from colorama import init, Fore, Style

init()

color_choice = input("Оберіть колір для форми реєстрації (RED, GREEN, BLUE): ").upper()

if color_choice == "RED":
    text_color = Fore.RED
elif color_choice == "GREEN":
    text_color = Fore.GREEN
elif color_choice == "BLUE":
    text_color = Fore.BLUE
else:
    text_color = Fore.WHITE

print(f"{text_color}Форма реєстрації")
print("------------------")
login = input("Введіть логін: ")
password = input("Введіть пароль: ")

text_color = Fore.YELLOW

print("------------------")
print(f"{text_color}Логін: {login}")
print(f"{text_color}Пароль: {password}")
print(Style.RESET_ALL)
