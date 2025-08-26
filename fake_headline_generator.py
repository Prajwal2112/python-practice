import random
# Create subjects
subject = [
    "Shahrukh Khan",
    "Virat Kohli",
    "Nirmala Sitaraman",
    "A Mumbai cat",
    "A Group of Monkeys",
    "Prime Ministed Modi",
    "Auto Rickshaw Driver from Delhi"
] 
action = [
    "launches",
    "cahcels",
    "dance with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"
]

place_or_things = [
    "at red fort",
    "in mumbai local Train",
    "a plate of samosa",
    "inside parliament",
    "at Ganga Ghat",
    "during IPL match",
    "at India Gate"
]

## Start the headline generation loop
while True :
    subjects = random.choice(subject)
    actions = random.choice(action)
    place_or_thing = random.choice(place_or_things)

    headline = (f" BREAKING NEWS: {subjects} {actions} {place_or_thing}")
    print("\n" + headline)

    user_input = input("\n Do you want another headline?(yes or no)").strip().lower()

    if user_input == "no":
        break

print("\n Thanks for using the Fake News Headline Generator. Have a fun  day ")