def word_count(string_input):
    words = string_input.split()
    return len(words)

def char_count(string_input):
    count_dict = {}
    string_input = string_input.lower()
    #string_input = string_input.split()
    chars = list(string_input)
    for char in chars:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict

def sorter(dict_input):
    # Convert dictionary to list of dictionaries
    list_of_dicts = []
    for char, count in dict_input.items():
        if char.isalpha():  # Only include alphabetical characters
            list_of_dicts.append({"char": char, "num": count})
    
    # Define the sort function
    def sort_on(item):
        return item["num"]
    
    # Sort the list
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts