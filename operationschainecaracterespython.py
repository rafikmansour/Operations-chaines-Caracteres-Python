# Concaténation
str1 = "Hello"
str2 = " World"
result = str1 + str2
print(result)  # Output: "Hello World"

# Répétition
str1 = "Hello"
result = str1 * 3
print(result)  # Output: "HelloHelloHello"

# Accès aux caractères
str1 = "Hello"
print(str1[0])  # Output: "H"

# Slicing
str1 = "Hello World"
sub_str = str1[0:5]  # Extraction des caractères de l'indice 0 à 4 (5 exclus)
print(sub_str)  # Output: "Hello"

# Longueur
str1 = "Hello"
length = len(str1)
print(length)  # Output: 5

# Mise en majuscule/minuscule
str1 = "Hello"
upper_case = str1.upper()
lower_case = str1.lower()
print(upper_case)  # Output: "HELLO"
print(lower_case)  # Output: "hello"

# Recherche et remplacement
str1 = "Hello World"
replaced_str = str1.replace("World", "Universe")
print(replaced_str)  # Output: "Hello Universe"

# Vérification de la présence de sous-chaînes
str1 = "Hello World"
if "Hello" in str1:
    print("La sous-chaîne 'Hello' est présente.")

# Suppression des espaces
str1 = "   Hello World   "
trimmed_str = str1.strip()
print(trimmed_str)  # Output: "Hello World"

# Découpage par délimiteur
str1 = "apple,orange,banana"
fruits_list = str1.split(",")
print(fruits_list)  # Output: ['apple', 'orange', 'banana']

# Formattage de chaîne
name = "John"
age = 30
formatted_str = "My name is {} and I am {} years old.".format(name, age)
# Ou en utilisant des f-strings
formatted_str = f"My name is {name} and I am {age} years old."
print(formatted_str)  # Output: "My name is John and I am 30 years old."
