import random

subjects = [
    "Hritik Roshan", "Virat Kohli", "A kerala cat", "A group of dogs", "Prime minister modi", "Ola driver","shah ruk khan"
    "Dhanush", "3 movie", "Spider man" , "A group of monkeys", "A group of cows", "A group of buffaloes", "A group of elephants", "A group of lions"
]

actions = [
    "running fast", "dances with", "orders", "eats", "sleeps", "launches", "declares war on", "celebrates", "typing", "smiling with happiness", "by seeing","crying after seeing", "laughing after seeing", "jumping with joy after seeing"
]

places_or_things = [
    "at Red Fort", "in Mumbai Local Train", "a plate of kachori", "inside parliament", "at river GANGA", "at India Gate", "during world war","at Taj Mahal", "at a wedding", "at a birthday party", "at a cricket match", "at a football match", "at a basketball match", "at a hockey match"
]

#headlines
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)


    headline = f"Breaking News: {subject} {action} {place_or_thing}"
    print("\n" + headline)

    # validate response: accept 'y', 'yes', 'n', 'no' (empty = yes)
    exit_loop = False
    while True:
        user_input = input("\nDo you want another headline? (y/n) ").strip().lower()
        if user_input in ("n", "no"):
            exit_loop = True
            break
        if user_input in ("y", "yes", ""):
            break
        print("Please enter 'y' or 'n'.")

    if exit_loop:
        break

print("\nThanks for using the fake news Headline Generator. Have a fun day")
        
