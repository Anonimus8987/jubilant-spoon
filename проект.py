all_product = {'Весь склад': {}}
korzinka = []

while True:
    admin = input('Что хотите сделать')
    if admin.lower() == 'Добавить':
        product_name = input('Названия продукта:')
        product_count = int(input('Количество:'))
        all_product['Весь склад'][product_name] = product_count
        print('Продукт успешно добавлен!')
    elif admin.lower == 'продукты':
        print(all_product)
    else:
        print('Неизвестная операция')    
        
        print(all_product)

        chto_kupit = input()


        print(korzinka)