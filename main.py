
with open("input/invited_names.txt") as names_file:
    names = list(names_file.read().splitlines())
    # print(names)

with open("input/letter_template.txt") as letter_file:
    letter = letter_file.read()
    for name in names:
        n_letter = letter.replace("[Name]", name).strip()
        # file_name = f"{name}_mail.txt"
        with open("output/ready_to_send//" f"{name}_mail.txt", mode="w") as ready_letters:
            letters = ready_letters.write(n_letter)
