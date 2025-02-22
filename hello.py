print("Hello, World!")

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

""" (b[2:5]) after 2 letters till 5 letters """
b = "Hello, World!"
print(b[2:5])

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = " Hello, World! "
print(a.strip())

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(10 + 5)

x = 5
y = 3
print(x - y)

x = 5
y = 2
print(x % y)

x = 2
y = 5
print(x ** y) #same as 2*2*2*2*2

x = 15
y = 2
print(x // y)

x = 5
print(type(x))

print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

thislist = ["apple", "banana", "cherry"]
print(thislist)
print(len(thislist))
print(type(thislist))

thislist = list(("apple", "banana", "cherry"))
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

mylist = ['apple', 'banana', 'cherry']  # Step 1: Create a list
mylist[0] = 'kiwi'  # Step 2: Change the first element (index 0)
print(mylist[1])  # Step 3: Print the second element (index 1)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)