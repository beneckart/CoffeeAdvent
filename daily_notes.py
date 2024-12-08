def get_manual_notes():
    db = {}
    db[1] = {
        'Ben': 'silky smooth mouthfeel, light cranberry, orange peel, pu-erh tea. sweeter as it cools',
        'Charlotte': 'smells like cedar. dark chocolate, cranberry. Walnut. In that order',
        'Shane': "Sweet, lower acid, but balanced with a  chocolate, candied orange, teensy weensy honeysuckle thing going on. A little too roasty but we'll look the other way because it's packed with holiday spirit.",
        'Shervlin': "Smell: Fermented tropical fruit, breadfruit, butterscotch Taste:Durian, guava, white tea, cantaloupe rind. ",
        'Brian': "I don't think I got a good extraction on this one. The flavor is pretty flat. Green grape, unripe peach, light blue gatorade",
        'Mom': "earthy, wet rocks, unburnt charcoal",
        'Dad': "earthy, round on the tongue, hits middle first then tip, not bitter, just a hint of christmas spice, not quite ripe cherries",
        'Taster': """Loads of florals, juicy stonefruit""",
        'Onyx': "Baked Apple | Earl Grey | Baker's Chocolate | Berries"
    }

    db[2] = {
        'Brian': "dark chocolate, orange peel, raisins, hazelnut",
        'Shane': "Dessert. Fudge and cocoa powder. Rich, juicy mouthfeel, like a big dry red wine.",
        'Mom': "sour, ground. celery and something sour like  buttermilk and mango. roasted nuts and sweet potatoes",
        'Dad': "dry clean hay in summer, dark chocolate, s'mores toasted chocolate marshmallows,  smooth dark chocolate with a pleasant aftertaste",
        'Ben': "cacao, dry, woody, tomato soup, licorice, prune",
        'Charlotte': "smells like currants and fresh laundry, tastes like black cherry, prune, dry",
        'Shervlin': """Smell: Warm milk
Taste: Milk chocolate (very milky), smores
Shervin rating: 5.5
Caitlin rating: 5.5""",
        'Taster': """Sweet fruit up front, Rich chocolate, nutty base""",
        'Onyx':"Strawberry | Wine | Dark Chocolate | Lime"
    }

    db[3] = {
        'Ben': """sweet tea, light molasses, raisin, sweet potato, asparagus""",
        #'Charlotte': """""",
        #'Aleda':"""""",
        'Shane': """Wee little beans, prob Ethiopian. Light bodied. Got some white floral, jasmine early on and then some serious lemon acidity as it cooled, maybe a little white peach. Black tea, chamomile, lemon. I feel like I could use a cup of coffee to wash this down. But Ben, in an attempt to try to pad my scores (and to make your work easier), I'll cut the fluff and just go with: black tea, chamomile, lemon.""",
        'Shervlin': """Smell: Orange Blossom, Jasmine
Taste: Green apple, bubble gum, Matcha green tea, lemongrass
Shervin Rating: 6.5
Caitlin Rating: 7.5""",
        'Brian': """lightly vegetal, snap peas, strawberry, apple pie, lemon custard 
soft mouthfeel with a round body""",
        'Mom': """On her way to Orange Beach to go shelling""",
        'Dad': """Beans - dried green vegetable, Ground - meaty like beef brisket, Brew - stone fruit, apricots""",
        'Taster': """Sweet, tea like flavors, stonefruit""",
        'Onyx': "Jasmine | Apricot | Honey | Tea-Like"
    }

    db[4] = {
        'Ben': """at the start I taste something sweet, something vegetal. festive. like red grape and green beans. as it cools, juicy sweet strawberry and other berries coming through. oily viscous mouthfeel. I really like this one. grade: A-""",
        # 'Charlotte': """""",
        # 'Aleda':"""""",
        'Shane': """Not a fan. I got some ripe cherry  and cinnamon on the nose during brewing but that was likely a mirage. On taste, I’m getting some sour, mostly green, vegetal vibes. Rather than a clean, citrusy finish, I’m getting a weird meaty (not the good, roasty Maillard kind, but more of the leftover hotdog water kind), cereal finish.""",
        'Shervin': """Bergamot, black tea, whole roasted cocao bean, prune. Dry mouthfeel. Wet fingerfeel.
Rating: 6/10""",
        'Caitlin':"""Indistinct nuts and spices with a hint of vanilla and the ghost of apple
Rating: 6/10""",
        'Brian': """Smells like chicken soup
Tasting notes: walnut, roasted carrot, pear, cocoa powder""",
        #'Mom': """""",
        'Dad': """Beans - sweet fruity cherries, Ground - citrus fruit orange, Brew - fruity mulled wine, warm sangria""",
        'Taster': """Citrus, Grapefruit, black currant, blackberries""",
        'Onyx': "Grapefruit | Plum | Sugar Cane | Juicy"


    }

    db[5] = {
        'Ben': """Smells musty. Like moist gym socks under a McDonalds heat lamp. Taste: Bitter melon, anise, date. Kinda astringent. Maybe some milk chocolate and honey peeking through at the end. Grade: C-""",
        'Charlotte': """Mild to no smell, light pepper
tobacco, roasted hazelnut, dash o pomegranate""",
        'Shane': """Notes: cloyingly musty/moldy cardboard, hints of nutty, stale cocoa powder and red/purple fruit like raisin or prune. Green apple type acidity (which makes no sense if the fruit is red/purple 🤷).
Rating: 5/10
Circumlocution: I really didn't like this coffee at first; I couldn't get past the dank greyness. But it started tasting a little cleaner and clearer as it cooled and some of the nuttiness and fruit came out.""",
        'Shervin': """Roasted senmacha tea, raspberry, sorrel aka tasty clover""",
        'Caitlin': """Vegetal notes like a pile of Alfalfa or lemongrass, lemon rind, hint of tart cherry""",
        'Brian': """toffee, grapefruit, green apple, tart raspberries""",
        'Aleda': """Sour, ashy, floral""",
        #'Mom': """""",
        'Dad': """Beans - deep rich chocolate, Ground - much lighter aroma, some fruit, Brew - lightly flavored, friendly flavor without bitter bite a little sour fruit at the end""",
        'Taster': """Sweet cherry, Malic Acidity, Red Apple, Honeysuckle, Hazelnut finish""",
        'Onyx': "Chamomile | Raw Sugar | Apple | White Flower"
    }

    db[6] = {
        'Ben': """Beans: lilac, rose. Grounds: korean bbq (kalbi). Taste: shiitake, cacao, sour milk, miso, mud""",
        'Charlotte': """Smells like the deck after a rain, tart cherry and gets more sour towards the end, malt, a pinch of pecan""",
        'Brian': """Pineapple, lemon, grapefruit. got distracted and let this cool and I'm just getting tons of acidity""",
        'Aleda':"""nutty""",
        'Shane': """Mouthfeel: robust, juicy, chewy. 
Tasting Notes: brown sugar (molasses, cacao, carob), port, and brown warming spices. Raspberry undertones, with a distinct pineapple juice thing (tepache?).""",
        'Shervin': """Plum, crisp green apple, tomato, nutmeg, agave. Sweet and savory with a hint of spice""",
        'Caitlin': """Sour fermented grapes at the start, cools to chocolate covered strawberries or maybe strawberries and cream, sweet fruit.
""",
        #'Mom': """""",
        'Dad': """Day 6 - Beans - sweet fruit, Ground - citrus fruit, Brew - very sour citrus, sour patch kids, astringent, middle back of tongue """,
        'Taster': """Yellow Pineapple, orange peach, red cherry, strawberry""",
        'Onyx': "Concord Grape | Demerara Sugar | Rose | Dark Chocolate"
    }

    db[7] = {
        'Ben': """Blueberry, lavender, rose water. Seems like a classic ethiopian light roast. B+""",
        #'Charlotte': """""",
        'Brian': """Raspberry, tomato soup, blackberry, black pepper
When it was hot it gave me big tomato soup/ minestrone vibes""",
        'Aleda':"""grapefruit sour at the front spices, savory at the end """,
        'Shervin': """Black cherry, rose, berry compote. Tastes roasty and red-fruity
6/10""",
        'Caitlin': """Candy cane, mint, vegetal""",
        #'Mom': """""",
        'Dad': """Beans - rich deep, Ground - green vegtable, Brew - cherry tomato, asparagus, soup. Liked this one a lot""",
        'Shane': """Mouthfeel: light, clean
Tasting notes: egg custard and tropical fruit (lime, kiwi, lychee, clementine, banana). """,
        'Taster': """Floral and sweet aroma. Strawberry, peach jam, black tea""",
        'Onyx': "Mixed Berries | Jasmine | Plum | Pineapple"
    }

    db[8] = {
        'Ben': """""",
        'Charlotte': """""",
        'Brian': """""",
        'Aleda':"""""",
        'Shervin': """""",
        'Caitlin': """""",
        'Mom': """""",
        'Dad': """""",
        'Shane': """""",
        'Onyx': "Concord Grape | Vanilla | Pomegranate | 60% Dark Chocolate",
        'Taster': """Juicy, Black Currant, dark cherry, red berries. Floral berry"""
    }

    db[9] = {
        'Ben': """""",
        'Charlotte': """""",
        'Brian': """""",
        'Aleda':"""""",
        'Shervin': """""",
        'Caitlin': """""",
        'Mom': """""",
        'Dad': """""",
        'Shane': """""",
        'Onyx': ""
    }

    return db