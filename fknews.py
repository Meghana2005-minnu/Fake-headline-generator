import random

subjects = [
    "Hritik Roshan", "Virat Kohli", "A kerala cat", "A group of dogs", "Prime minister modi", "Ola driver","shah ruk khan"
    "Dhanush", "3 movie", "Spider man"
]

actions = [
    "running fast", "dances with", "orders", "eats", "sleeps", "launches", "declares war on", "celebrates", "typing", "smiling with happiness", "by seeing"
]

places_or_things = [
    "at Red Fort", "in Mumbai Local Train", "a plate of kachori", "inside parliament", "at river GANGA", "at India Gate", "during world war"
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
        
