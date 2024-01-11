def dictionary_operations():
    # Create a dictionary
    my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

    # Print the original dictionary
    print("Original Dictionary:")
    print(my_dict)

    # Accessing values
    print("\nAccessing values:")
    print("Name:", my_dict['name'])
    print("Age:", my_dict['age'])
    print("City:", my_dict['city'])

    # Modifying values
    print("\nModifying values:")
    my_dict['age'] = 31
    print("Updated Age:", my_dict['age'])

    # Adding a new key-value pair
    print("\nAdding a new key-value pair:")
    my_dict['gender'] = 'Male'
    print("Updated Dictionary:", my_dict)

    # Removing a key-value pair
    print("\nRemoving a key-value pair:")
    removed_value = my_dict.pop('city')
    print("Removed City:", removed_value)
    print("Updated Dictionary:", my_dict)

    # Dictionary keys and values
    print("\nDictionary keys and values:")
    print("Keys:", my_dict.keys())
    print("Values:", my_dict.values())

    # Checking if a key is in the dictionary
    print("\nChecking if a key is in the dictionary:")
    print("Is 'name' in the dictionary?", 'name' in my_dict)
    print("Is 'address' in the dictionary?", 'address' in my_dict)

if __name__ == "__main__":
    dictionary_operations()
