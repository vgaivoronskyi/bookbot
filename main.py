def words_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    res = {}
    for ch in text.lower():
        if ch not in res:
            res[ch] = 1
        else:
            res[ch] += 1
    return res

def sort_on(dict):
    return dict["count"]

def convert_and_sort(dict):
    res = []
    for k, v in dict.items():
        res.append({"char" : k, "count" : v})
    return res
 
with open ("books/frankenstein.txt") as f:
    file_contents = f.read()
    w_count = words_count(file_contents)
    chars = character_count(file_contents)
    data = convert_and_sort(chars)
    data.sort(reverse=True, key=sort_on)
    print(data)
    print("--Begin report of books/frankenstein.txt ---")
    print(str(w_count) + " words found in the document\n")
    for el in data:
        if el['char'].isalpha():
            print(f"The '{el['char']}' character was found {el['count']} times")
    print("--End report ---")
