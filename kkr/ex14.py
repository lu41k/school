string = open(file="24-191.txt", mode="r").readline()

string_without_A = string.replace("A", " ")

count: int = 0
for word in string_without_A.split(" "):
    word = word.split("B")

    for little_word in word:
        if len(little_word) >= 20 or little_word.count("F") == 2:
            index_of_word = string.find(little_word)

            if string[index_of_word - 1] == "A" and string[index_of_word + len(little_word)] == "B":
                count += 1


print(count)
