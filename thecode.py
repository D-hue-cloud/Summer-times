temp=int(input("So what's the temperature where you are rn\n   "))
if 10<temp<20:
    print("England weather!")
    print("I would recommend a thin coat with yor t-shirts and jeans")
elif 20<temp<25:
    print("Starting to warm up a bit, I see... :)")
    print("I would reccoment a t-shirt and jeans\nbut maybe bring a spring jacket just in case")
elif 5<temp<10:
    print("Getting a bit chilly eh?")
    print("What about a thick spring coat and a beanie?")
elif temp>25:
    print("That's summer for ya!")
    print("Just a t-shirt and shorts will be just fine!\nmaybe some sunglasses")
elif 0<temp<5:
    print("Its beginning to feel a lot like Christmas!")
    print("Perhaps a winter coat and a beanie over your Xmas jumper")
elif temp<0:
    print("Whoa! Are you in the north pole?")
    print("LAYERS!! Add on thermal under-wear, jumpers, sweaters, joggers,\nthickest coat you can find, beanie and gloves")
bool(input("Has this been helpful? T/F  "))
print("Thanks for feedback!")