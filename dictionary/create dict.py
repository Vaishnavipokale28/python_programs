def create_dictionary():
    dictionary = {}
    num_entries = int(input("Enter the number of dictionary entries: "))

    for i in range(num_entries):
        key = input("Enter key for entry {}: ".format(i + 1))
        value = input("Enter value for entry {}: ".format(i + 1))
        dictionary[key] = value

    return dictionary



my_dictionary = create_dictionary()
print(my_dictionary)
