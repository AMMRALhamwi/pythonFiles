books = []
wishs = []
got_it = []
books.append(input("Enter the name of a book you own : \n "))

first = (
    input(' Enter the name of another book you own :(or press Enter to pass)'))
if first != '':
    books.append(first)
print("Your library :")
print(books)
second = input(
    'Enter the name of a book you wish to have in the future :(or press Enter to pass)')
if second != '':
    wishs.append(second)
print("your wish list is :")
print(wishs)
three = input(
    'Enter the name of another book you wish to have (or press (Enter to sikp)')
if three != '':
    wishs.append(three)
print('Your wish list :')
print(wishs)

four = input(
    "Enter the name of a book from your wishlist that youve got it : (or press Enter to skip)")
if four != "" and four in wishs:
    books.append(four)
    wishs.remove(four)
print('library apdeted')
print(books)
print('wish list updated')
print(wishs)
five = input(
    "Enter the name of a book from your library you wish to donate : (or press Enter to skip)")
if five != "" and five in books:
    books.remove(five)
print('final library after donttion :')
print(books)


# print('library apdated :')
# print(books)
# if ""
