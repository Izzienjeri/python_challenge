def count_vowels(text):
    vowel_count = 0
    vowels = "aeiou"
    
    for char in text:
        if char.lower() in vowels:
            vowel_count += 1  

    return vowel_count

print(count_vowels("izzie"))  