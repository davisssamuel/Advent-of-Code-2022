# Part 1
total_calories = list()
with open("input.txt") as infile:
    data = infile.readlines()
    total = 0
    for line in data:
        if line != '\n':
            total += int(line)
        else:
            total_calories.append(total)
            total = 0
print(f"MAX: {max(total_calories)}")

# Part 2
sum = sum(sorted(total_calories)[len(total_calories) - 3:len(total_calories)])
print(f"TOTAL OF TOP THREE: {sum}")
