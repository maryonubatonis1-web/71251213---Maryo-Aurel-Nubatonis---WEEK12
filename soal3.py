fname = input("Enter a file name: ")
fhand = open(fname)

jam = {}

for line in fhand:
    if line.startswith("From "):
        words = line.split()
        time = words[5]
        h = time.split(":")[0]
        jam[h] = jam.get(h, 0) + 1

for k in sorted(jam):
    print(k, jam[k])

    