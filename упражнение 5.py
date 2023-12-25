small = float(input("Сколько бутылок маленького размера вы хотите сдать? "))
big = float(input("Сколько бутылок большого размера вы хотите сдать? "))
result_small = small * 0.10
result_big = big * 0.25
all = result_small+result_big
r = round(all,2)
print(f"Пользователь сдает {small} маленьких бутылок и {big} больших бутылок что в сумме получается ${r}")