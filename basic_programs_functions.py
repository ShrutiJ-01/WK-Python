#find even numbers fromt he list
def has_even_number(numbers):
    for num in numbers:
        if num % 2 == 0:
            print("Found even number")
            return True

# Create a list of even numbers foun in numbers[]
def get_even_numbers(numbers):
    even_numbers=[]
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

#Take a string and find out the vowels in it
def find_vowels_in_string():
    str = input("Enter a string ")
    str.casefold()
    vowels = "aeiou"
    vowel_count = [vowel for vowel in str if vowel in vowels]
    print(f"The vowels are {len(vowel_count)}")

#count the number of times a vowel is repeated
def get_vowel_frequency():
    str1 = input("Enter a string ")
    str1.casefold()
    vowels = "aeiou"
    vowel_freq = {}.fromkeys(vowels,0)
    for char in str1:
        if char in vowels:
            vowel_freq[char] += 1
    print(f"The vowel frequencies are : {vowel_freq}")



has_even_number([23,65,78,43,36,23])
print(get_even_numbers([23,65,78,43,36,23]))
find_vowels_in_string()
get_vowel_frequency()