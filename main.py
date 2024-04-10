# Write a string to a file on a new line every time in Python

# ✅ Newer syntax (better)

with open('example.txt', 'w', encoding='utf-8') as my_file:
    my_file.write('first line' + '\n')
    my_file.write('second line' + '\n')
    my_file.write('third line' + '\n')

# -----------------------------------------------------

# ✅ Older syntax (not recommended)

file = open('example.txt', 'w', encoding='utf-8')

file.write('first line' + '\n')
file.write('second line' + '\n')
file.write('third line' + '\n')

file.close()