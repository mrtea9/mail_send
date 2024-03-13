# Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

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
