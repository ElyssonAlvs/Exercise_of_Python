print('''Choice the product to want eat, type your food number : 
        1 -> Hot Dog
        2 -> X-Salad
        3 -> X-Bacon
        4 -> Plain toast
        5 -> Soda''')
food = int(input('Food : '))
amount = int(input('Choice the amount of food : '))
price = int
if food == 1:
    price = 4 * amount
elif food == 2:
    price = 4.5 * amount
elif food == 3:
    price = 5 * amount
elif food == 4:
    price = 2 * amount
elif food == 5:
    price = 1.5 * amount
print('Total : {}'.format(price))
