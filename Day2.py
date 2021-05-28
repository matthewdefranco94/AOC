

# r will ignore escape characters
with open(r'C:\Users\Matthew\Desktop\AOC\day2input.txt', 'r') as file:
    entries = file.read().splitlines()

#-# letter: letters


valid_passwords_count = 0

for entry in entries:
    line_strs = entry.split(" ")
    no_dash = line_strs[0].split('-')
    min_char = int(no_dash[0])
    max_char = int(no_dash[1])
    letter = line_strs[1][0]
    password = line_strs[2]
    matched_count = password.count(letter)

    if matched_count <= max_char and matched_count >= min_char:
        valid_passwords_count += 1


valid_passwords_count_2 = 0
for x in entries:
    line_strs = x.split(' ')
    no_dash = line_strs[0].split('-')
    #cant subtract and integer from a string, so must be outside of conversion(After)
    char_pos1 = int(no_dash[0]) - 1
    char_pos2 = int(no_dash[1]) - 1
    letter = line_strs[1][0]
    password = line_strs[2]
    char_one = password[char_pos1]
    char_two = password[char_pos2]

    #check operator precedence for XOR, set in parenthese to compare
    if (char_one == letter) ^ (char_two == letter):
        valid_passwords_count_2 += 1


print(valid_passwords_count_2)









# print(valid_passwords_count)



    # print(no_dash)