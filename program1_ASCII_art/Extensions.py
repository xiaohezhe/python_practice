from colorama import init, Fore, Back, Style

# init(strip=False)
init(autoreset=True)

print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Fore.LIGHTBLUE_EX + 'HelloWorLd')