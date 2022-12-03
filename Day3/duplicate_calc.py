infile = open("input.txt")
data = infile.readlines()
infile.close()

sum = 0

# Part 1
# for ruck in data:
#     ruck = ruck.strip()
#     first_compartment, second_compartment = ruck[:len(ruck)//2], ruck[len(ruck)//2:]
#     for item in first_compartment:
#         if item in second_compartment: # find duplicate in both compartments
#             if item.isupper():
#                 sum += (ord(item.lower()) - 96) + 26
#                 break
#             else:
#                 sum += ord(item) - 96
#                 break

# Part 2
for i in range(0, len(data), 3):
    group = data[i:i + 3]
    duplicate_items = str()
    for item in group[0].strip():
        if item in group[1].strip():
            duplicate_items += item
    duplicate_items = "".join(set(duplicate_items))
    for item in duplicate_items:
        if item in group[2].strip():
            if item.isupper():
                sum += (ord(item.lower()) - 96) + 26
                break
            else:
                sum += ord(item) - 96
                break

print(f"SUM: {sum}")