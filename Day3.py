# r will ignore escape characters
with open(r'C:\Users\Matthew\Desktop\AOC\day3input.txt', 'r') as file:
    entries = file.read().splitlines()

# print(entries)

tree_char = '#'
gap_char  = '.'

right_shift = 3

x = 0
tree_count = 0

for row in entries:
    if row[x] == tree_char:
        tree_count += 1

    x = (x + right_shift) % len(row)

print(tree_count)


# Test Cases

# cur_x = 0                           x..#.
# cur_x = (0 + 3) % 5  = 3            ...x.
# cur_x = (3 + 3) % 5 = 6 % 5 = 1     .x.#.
# cur_x = (1 + 3) % 5 = 4 % 5 = 4     ...#x

# 0 % 5 = 0
# 1 % 5 = 1
# 2 % 5 = 2
# 3 % 5 = 3
# 4 % 5 = 4
# 5 % 5 = 0

# 50 % 5 = 0
# 51 % 5 = 1
# 11 % 5 = 1

# current index + offset % row length = new index
