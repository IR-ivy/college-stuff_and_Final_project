while True:
    flavor = {'Vanilla': 1, 'Chocolate': 1, 'Cookies & Cream': 1, 'Rocky Road': 1, 'Cookies Dough': 1,
              'Cinacholic': 2, 'Apple Py': 2, 'Mint Chocolate Chip': 1, 'Strawberry': 1, 'Butter Pecan': 1,
              'Birthday Cake': 1, 'Banana Split': 1, 'Vanilla & Py': 2, 'Almondjoy': 1, 'Maple Walnut': 1,
              'Mango': 1,} #$1 per scoop
    
    milkshakes_small = {'Vanilla Milkshake': 3, 'Chocolate  Milkshake': 3, 'Cookies & Cream Milkshake': 3, 'Rocky Road Milkshake': 3, 'Cookies Dough Milkshake': 3,
              'Cinacholic Milkshake': 3, 'Apple Py Milkshake': 3, 'Mint Chocolate Chip Milkshake': 3, 'Strawberry Milkshake': 3, 'Butter Pecan': 1,
              'Birthday Cake': 1, 'Banana Split': 1, 'Vanilla & Py': 2, 'Almondjoy': 1, 'Maple Walnut': 1,
              'Mango': 1,}#$3 small $3.50 medium $4 large
    
    milkshakes_medium = {'Vanilla Milkshake': 3.5, 'Chocolate  Milkshake': 3.5, 'Cookies & Cream Milkshake': 3.5, 'Rocky Road Milkshake': 3.5, 'Cookies Dough Milkshake': 3.5,
              'Cinacholic Milkshake': 3.5, 'Apple Py Milkshake': 3.5, 'Mint Chocolate Chip Milkshake': 3.5, 'Strawberry Milkshake': 3.5, 'Butter Pecan': 1,
              'Birthday Cake': 1, 'Banana Split': 1, 'Vanilla & Py': 2, 'Almondjoy': 1, 'Maple Walnut': 1,
              'Mango': 1,}
    
    milkshakes_Large = {'Vanilla Milkshake': 4, 'Chocolate  Milkshake': 4, 'Cookies & Cream Milkshake': 4, 'Rocky Road Milkshake': 4, 'Cookies Dough Milkshake': 4,
              'Cinacholic Milkshake': 4, 'Apple Py Milkshake': 4, 'Mint Chocolate Chip Milkshake': 4, 'Strawberry Milkshake': 4, 'Butter Pecan': 1,
              'Birthday Cake': 1, 'Banana Split': 1, 'Vanilla & Py': 2, 'Almondjoy': 1, 'Maple Walnut': 1,
              'Mango': 1,}
    
    froyo = {'Vanilla Froyo': 3, 'Chocolate Froyo': 3, 'Strawberry Froyo': 3, 'Berry Froyo': 3, 'Cherry Froyo': 3, 'Banana Froyo': 3, 'Mango Froyo': 3,
              'Apple Froyo': 3, 'Watermelon Froyo': 3}#$3
    
    sandwiches_chocolate_cookie = {'Vanilla Chocolate cookie': 2.5, 'Chocolate Chocolate cookie': 2.5, 'Cookies & Cream Chocolate cookie': 2.5, 'Rocky Road Chocolate cookie': 2.5,
                  'Cookies Dough Chocolate cookie': 2.5, 'Cinacholic Chocolate cookie': 3, 'Apple Py Chocolate cookie': 3, 'Mint Chocolate Chip Chocolate cookie': 2.5,
                  'Strawberry Chocolate cookie': 2.5, 'Butter Pecan Chocolate cookie': 2.5, 'Birthday Cake Chocolate cookie': 2.5, 'Banana Split Chocolate cookie': 2.5,
                  'Vanilla & Py Chocolate cookie': 3, 'Almondjoy Chocolate cookie': 2.5, 'Maple Walnut Chocolate cookie': 2.5, 'Mango Chocolate cookie': 2.5,}#$2.50
    
    sandwiches_chocolate_chip_cookie = {'Vanilla Chocolate chip cookie': 2.5, 'Chocolate Chocolate chip cookie': 2.5, 'Cookies & Cream Chocolate chip cookie': 2.5,
        'Rocky Road Chocolate chip cookie': 2.5, 'Cookies Dough Chocolate chip cookie': 2.5, 'Cinacholic Chocolate chip cookie': 3,
        'Apple Py Chocolate chip cookie': 3, 'Mint Chocolate Chip Chocolate chip cookie': 2.5, 'Strawberry Chocolate chip cookie': 2.5, 'Butter Pecan Chocolate chip cookie': 2.5,
        'Birthday Cake Chocolate chip cookie': 2.5, 'Banana Split Chocolate chip cookie': 2.5, 'Vanilla & Py Chocolate chip cookie': 3, 'Almondjoy Chocolate chip cookie': 2.5,
        'Maple Walnut Chocolate cookie': 2.5, 'Mango Chocolate cookie': 2.5,}
    
    toppings = {'Cookie crumble':0.25, 'Chocolate chip':0.25, 'Chocolate drizzle':0.25, 'Strawberry drizzle':0.25, 'Carmel drizzle':0.25,
                 'Oreo crumble':0.25, "Monty's drizzle":0.5}#$0.25 per topping special topping $0.50
    
    popsicles = {}#$1
    icecream_cakes = {}#$15
    order = input(f'Please input your order from this menu {flavor}.')