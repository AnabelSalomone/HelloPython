import random

secret_philosopher = "Immanuel Kant"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False


hints = [
    "He was a philosopher from the Lumieres period ",
    "He was from Prussia ",
    "He wrote a lot of critics ",
    "He wrote about categories "
]


while guess != secret_philosopher and not out_of_guesses:
    if guess_count < guess_limit:
        generate_id = random.randint(0, 3)
        previous_id = generate_id
        guess = input(hints[generate_id])
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Sorry! you lose")
else:
    print("Yes! Well done")
