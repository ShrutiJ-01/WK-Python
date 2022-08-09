numbers=[23,65,78,43,36,23]
#find even numbers fromt he list
for num in numbers:
    if num % 2 == 0:
        print("Found even number")
        break

# Create a list of even numbers foun in numbers[]
even_numbers=[]
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(f"List of even numbers is {even_numbers}")

#Take a string and find out the vowels in it
str = input("Enter a string ")
str.casefold()
vowels = "aeiou"
length = 0

vowel_count = [vowel for vowel in str if vowel in vowels]
print(f"The vowels are {len(vowel_count)}")

#count the number of times a vowel is repeated
vowel_freq = {}.fromkeys(vowels,0)

for char in str:
    if char in vowels:
        vowel_freq[char] += 1

print(f"The vowel frequencies are : {vowel_freq}")
