while True:
    flavor = {'Vanilla': 1, 'Chocolate': 1, 'Cookies & Cream': 1, 'Rocky Road': 1, 'Cookies Dough': 1,
              'Cinacholic': 2, 'Apple Py': 2, 'Mint Chocolate Chip': 1, 'Strawberry': 1, 'Butter Pecan': 1,
              'Birthday Cake': 1, 'Banana Split': 1, 'Vanilla & Py': 2, 'Almondjoy': 1, 'Maple Walnut': 1,
              'Mango': 1, }  # $1 per scoop

    milkshakes_small = {'Vanilla Milkshake': 3, 'Chocolate  Milkshake': 3, 'Cookies & Cream Milkshake': 3,
                        'Rocky Road Milkshake': 3, 'Cookies Dough Milkshake': 3,
                        'Cinacholic Milkshake': 3.25, 'Apple Py Milkshake': 3.25, 'Mint Chocolate Chip Milkshake': 3,
                        'Strawberry Milkshake': 3, 'Butter Pecan': 3,
                        'Birthday Cake': 3, 'Banana Split': 3, 'Vanilla & Py': 3.25, 'Almondjoy': 3.25, 'Maple Walnut': 3.25,
                        'Mango': 3.25, }  # $3 small $3.50 medium $4 large

    milkshakes_medium = {'Vanilla Milkshake': 3.5, 'Chocolate  Milkshake': 3.5, 'Cookies & Cream Milkshake': 3.5,
                         'Rocky Road Milkshake': 3.5, 'Cookies Dough Milkshake': 3.5,
                         'Cinacholic Milkshake': 3.75, 'Apple Py Milkshake': 3.75, 'Mint Chocolate Chip Milkshake': 3.5,
                         'Strawberry Milkshake': 3.5, 'Butter Pecan': 3.5,
                         'Birthday Cake': 3.5, 'Banana Split': 3.5, 'Vanilla & Py': 3.75, 'Almondjoy': 3.5, 'Maple Walnut': 3.5,
                         'Mango': 3.5, }

    milkshakes_Large = {'Vanilla Milkshake': 4, 'Chocolate  Milkshake': 4, 'Cookies & Cream Milkshake': 4,
                        'Rocky Road Milkshake': 4, 'Cookies Dough Milkshake': 4,
                        'Cinacholic Milkshake': 4.25, 'Apple Py Milkshake': 4.25, 'Mint Chocolate Chip Milkshake': 4,
                        'Strawberry Milkshake': 4, 'Butter Pecan Milkshake': 4, 'Birthday Cake Milkshake': 4,
                        'Banana Split Milkshake': 4, 'Vanilla & Py Milkshake': 4.25, 'Almondjoy Milkshake': 4,
                        'Maple Walnut Milkshake': 4, 'Mango Milkshake': 4 }

    froyo = {'Vanilla Froyo': 3, 'Chocolate Froyo': 3, 'Strawberry Froyo': 3, 'Berry Froyo': 3, 'Cherry Froyo': 3,
             'Banana Froyo': 3, 'Mango Froyo': 3, 'Apple Froyo': 3, 'Watermelon Froyo': 3}  # $3

    sandwiches_chocolate_cookie = {'Vanilla Chocolate cookie': 2.5, 'Chocolate Chocolate cookie': 2.5,
                                   'Cookies & Cream Chocolate cookie': 2.5, 'Rocky Road Chocolate cookie': 2.5,
                                   'Cookies Dough Chocolate cookie': 2.5, 'Cinacholic Chocolate cookie': 3,
                                   'Apple Py Chocolate cookie': 3, 'Mint Chocolate Chip Chocolate cookie': 2.5,
                                   'Strawberry Chocolate cookie': 2.5, 'Butter Pecan Chocolate cookie': 2.5,
                                   'Birthday Cake Chocolate cookie': 2.5, 'Banana Split Chocolate cookie': 2.5,
                                   'Vanilla & Py Chocolate cookie': 3, 'Almondjoy Chocolate cookie': 2.5,
                                   'Maple Walnut Chocolate cookie': 2.5, 'Mango Chocolate cookie': 2.5, }  # $2.50

    sandwiches_chocolate_chip_cookie = {'Vanilla Chocolate chip cookie': 2.5, 'Chocolate Chocolate chip cookie': 2.5,
            'Cookies & Cream Chocolate chip cookie': 2.5, 'Rocky Road Chocolate chip cookie': 2.5,
            'Cookies Dough Chocolate chip cookie': 2.5, 'Cinacholic Chocolate chip cookie': 3,
            'Apple Py Chocolate chip cookie': 3, 'Mint Chocolate Chip Chocolate chip cookie': 2.5,
            'Strawberry Chocolate chip cookie': 2.5, 'Butter Pecan Chocolate chip cookie': 2.5,
            'Birthday Cake Chocolate chip cookie': 2.5, 'Banana Split Chocolate chip cookie': 2.5,
            'Vanilla & Py Chocolate chip cookie': 3, 'Almondjoy Chocolate chip cookie': 2.5,
            'Maple Walnut Chocolate cookie': 2.5, 'Mango Chocolate cookie': 2.5, }

    popsicles = {"Cherry": 1, "Watermelon": 1, "Banana": 1, "Lime": 1, "Apple": 1, "Strawberry": 1, "Grape": 1,
                 "Blue Raspberry": 1, "Lemon": 1, "Mango": 1}  # $1

    icecream_cakes = {"Vanilla Icecream cake": 15, "Chocolate Icecream cake": 15, "Oreo Icecream cake": 15,
                      "Ciniacholic": 17.5, "Apple Py": 17.5}  # $15

    toppings = {'Cookie crumble': 0.25, 'Chocolate chip': 0.25, 'Chocolate drizzle': 0.25, 'Strawberry drizzle': 0.25,
                'Carmel drizzle': 0.25, 'Oreo crumble': 0.25, "Monty's drizzle": 0.5, "Rainbow Sprinkles": 0.25,
                "Different colored sprinkles": 0.25}  # $0.25 per topping special topping $0.50
    menu = input("For our menu press 0 for Ice Cream Cones, 1 Ice cream toppings, 2 for milkshakes (small), 3 for "
                 "milkshakes (medium), 4 for milkshakes (large), 5 for froyo, 6 for Ice Cream Sandwiches with chocolate"
                 " cookies, 7 Ice Cream, Sandwiches with chocolate chip cookies, 8 for popsicles, 9 for ice cream cakes")
    if menu == 0:
        print(f"Here is our different icecream flavors and next to them are our prices, {flavor}")
    elif menu == 1:
        print(f"Here is our different toppings and next to them are our prices, {toppings}")
    elif menu == 2:
        print(f"Here is our different milkshake flavors and next to them are our prices {milkshakes_small}")
    elif menu == 3:
        print(f"Here are our different milkshake flavors and next to them are our prices {milkshakes_medium}")
    elif menu == 4:
        print(f"Here are our different milkshake flavors and next to them are our prices {milkshakes_Large}")
    elif menu == 5:
        print(f"Here is our different froyo flavors and next to them are our prices, {froyo}")
    elif menu == 6:
        print(f"Here is our different icecream sandwich flavors and next to them are our prices cookies {sandwiches_chocolate_cookie}")
    elif menu == 7:
        print(f"Here is our different icecream sandwich flavors and next to them are our prices cookies {sandwiches_chocolate_chip_cookie}")
    elif menu == 8:
        print(f"Here is our different popsicle flavors and next to them are our prices, {popsicles}")
    elif menu == 9:
        print(f"Here is our different icecream cake flavors and next to them are our prices, {icecream_cakes}")
    order = input(f'Please input your order from our menu showed above and any price that is higher than the ones around'
                  f' are our specialties or our original flavors.')

