
letter_location = '.\\Input\\Letters\\starting_letter.txt'
names_location = '.\\Input\\\\Names\\invited_names.txt'
ready_location = '.\\Output\\ReadyToSend\\'

with open(names_location) as file_names:
    names = file_names.read()

names = names.split()

with open(letter_location) as file:
    contents = file.read()

for name in names:
    result = contents.replace("[name]", name)
    final_location = ready_location + f"letter_for_{name}.txt"
    with open(final_location, 'w') as file_result:
        file_result.write(result)
