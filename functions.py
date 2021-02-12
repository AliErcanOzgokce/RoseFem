import random

def full():
    uppercase_letters = "ABCDEFGHIJKLMNOPRSTUVYZQW"
    lowercase_letters = uppercase_letters.lower()
    digits = "0123456789"
    symbols = "!'^#+$%&/{([)]=}?\\*-_,;`´<>|"
    upper, lower, nums, syms = True, True, True, True
    all = ""

    if upper:
        all += uppercase_letters
    if lower:
        all += lowercase_letters
    if nums:
        all += digits
    if syms:
        all += symbols
    length = int(input("What Is The Length Of Password:"))
    amount = int(input("How Much Password?:"))
    for x in range(amount):
        password = "".join(random.sample(all, length))
        print(password)
def only_upper():
    uppercase_letters = "ABCDEFGHIJKLMNOPRSTUVYZQW"
    lowercase_letters = uppercase_letters.lower()
    digits = "0123456789"
    symbols = "!'^#+$%&/{([)]=}?\\*-_,;`´<>|"

    upper, lower, nums, symbols = True, False, False, False

    all = ""

    if upper:
        all += uppercase_letters
    if lower:
        all += lowercase_letters
    if nums:
        all += digits
    if symbols:
        all += symbols
    length = int(input("What Is The Length Of Password:"))
    amount = int(input("How Much Password?:"))
    for x in range(amount):
        password = "".join(random.sample(all, length))
        print(password)
def only_lower():
    uppercase_letters = "ABCDEFGHIJKLMNOPRSTUVYZQW"
    lowercase_letters = uppercase_letters.lower()
    digits = "0123456789"
    symbols = "!'^#+$%&/{([)]=}?\\*-_,;`´<>|"
    length = int(input("What Is The Length Of Password:"))
    amount = int(input("How Much Password?:"))

    upper, lower, nums, symbols = False, True, False, False

    all = ""

    if upper:
        all += uppercase_letters
    if lower:
        all += lowercase_letters
    if nums:
        all += digits
    if symbols:
        all += symbols
    for x in range(amount):
        password = "".join(random.sample(all, length))
        print(password)
def only_nums():
    uppercase_letters = "ABCDEFGHIJKLMNOPRSTUVYZQW"
    lowercase_letters = uppercase_letters.lower()
    digits = "0123456789"
    symbols = "!'^#+$%&/{([)]=}?\\*-_,;`´<>|"
    length = int(input("What Is The Length Of Password:"))
    amount = int(input("How Much Password?:"))

    upper, lower, nums, symbols = False, False, True, False

    all = ""

    if upper:
        all += uppercase_letters
    if lower:
        all += lowercase_letters
    if nums:
        all += digits
    if symbols:
        all += symbols
    for x in range(amount):
        password = "".join(random.sample(all, length))
        print(password)
def only_syms():
    uppercase_letters = "ABCDEFGHIJKLMNOPRSTUVYZQW"
    lowercase_letters = uppercase_letters.lower()
    digits = "0123456789"
    symbols = "!'^#+$%&/{([)]=}?\\*-_,;`´<>|"
    length = int(input("What Is The Length Of Password:"))
    amount = int(input("How Much Password?:"))

    upper, lower, nums, syms = False, False, False, True

    all = ""

    if upper:
        all += uppercase_letters
    if lower:
        all += lowercase_letters
    if nums:
        all += digits
    if syms:
        all += symbols
    for x in range(amount):
        password = "".join(random.sample(all, length))
        print(password)
def upper_lower():
    uppercase_letters = "ABCDEFGHIJKLMNOPRSTUVYZQW"
    lowercase_letters = uppercase_letters.lower()
    digits = "0123456789"
    symbols = "!'^#+$%&/{([)]=}?\\*-_,;`´<>|"
    length = int(input("What Is The Length Of Password:"))
    amount = int(input("How Much Password?:"))
    upper, lower, nums, symbols = True, True, False, False

    all = ""

    if upper:
        all += uppercase_letters
    if lower:
        all += lowercase_letters
    if nums:
        all += digits
    if symbols:
        all += symbols
    for x in range(amount):
        password = "".join(random.sample(all, length))
        print(password)
def upper_nums():
    uppercase_letters = "ABCDEFGHIJKLMNOPRSTUVYZQW"
    lowercase_letters = uppercase_letters.lower()
    digits = "0123456789"
    symbols = "!'^#+$%&/{([)]=}?\\*-_,;`´<>|"
    length = int(input("What Is The Length Of Password:"))
    amount = int(input("How Much Password?:"))
    upper, lower, nums, symbols = True, False, True, False

    all = ""

    if upper:
        all += uppercase_letters
    if lower:
        all += lowercase_letters
    if nums:
        all += digits
    if symbols:
        all += symbols
    for x in range(amount):
        password = "".join(random.sample(all, length))
        print(password)
def upper_symbols():
    uppercase_letters = "ABCDEFGHIJKLMNOPRSTUVYZQW"
    lowercase_letters = uppercase_letters.lower()
    digits = "0123456789"
    symbols = "!'^#+$%&/{([)]=}?\\*-_,;`´<>|"
    length = int(input("What Is The Length Of Password:"))
    amount = int(input("How Much Password?:"))
    upper, lower, nums, symbols = True, False, False, True

    all = ""

    if upper:
        all += uppercase_letters
    if lower:
        all += lowercase_letters
    if nums:
        all += digits
    if symbols:
        all += symbols
    for x in range(amount):
        password = "".join(random.sample(all, length))
        print(password)
def lower_nums():
    uppercase_letters = "ABCDEFGHIJKLMNOPRSTUVYZQW"
    lowercase_letters = uppercase_letters.lower()
    digits = "0123456789"
    symbols = "!'^#+$%&/{([)]=}?\\*-_,;`´<>|"
    length = int(input("What Is The Length Of Password:"))
    amount = int(input("How Much Password?:"))
    upper, lower, nums, symbols = False, True, True, False

    all = ""

    if upper:
        all += uppercase_letters
    if lower:
        all += lowercase_letters
    if nums:
        all += digits
    if symbols:
        all += symbols
    for x in range(amount):
        password = "".join(random.sample(all, length))
        print(password)
def lower_symbols():
    uppercase_letters = "ABCDEFGHIJKLMNOPRSTUVYZQW"
    lowercase_letters = uppercase_letters.lower()
    digits = "0123456789"
    symbols = "!'^#+$%&/{([)]=}?\\*-_,;`´<>|"
    length = int(input("What Is The Length Of Password:"))
    amount = int(input("How Much Password?:"))
    upper, lower, nums, syms = False, True, False, True

    all = ""

    if upper:
        all += uppercase_letters
    if lower:
        all += lowercase_letters
    if nums:
        all += digits
    if syms:
        all += symbols
    for x in range(amount):
        password = "".join(random.sample(all, length))
        print(password)
def nums_symbols():
    uppercase_letters = "ABCDEFGHIJKLMNOPRSTUVYZQW"
    lowercase_letters = uppercase_letters.lower()
    digits = "0123456789"
    symbols = "!'^#+$%&/{([)]=}?\\*-_,;`´<>|"
    length = int(input("What Is The Length Of Password:"))
    amount = int(input("How Much Password?:"))
    upper, lower, nums, syms = False, False, True, True

    all = ""

    if upper:
        all += uppercase_letters
    if lower:
        all += lowercase_letters
    if nums:
        all += digits
    if syms:
        all += symbols
    for x in range(amount):
        password = "".join(random.sample(all, length))
        print(password)
def upper_lower_nums():
    uppercase_letters = "ABCDEFGHIJKLMNOPRSTUVYZQW"
    lowercase_letters = uppercase_letters.lower()
    digits = "0123456789"
    symbols = "!'^#+$%&/{([)]=}?\\*-_,;`´<>|"
    length = int(input("What Is The Length Of Password:"))
    amount = int(input("How Much Password?:"))
    upper, lower, nums, symbols = True, True, True, False

    all = ""

    if upper:
        all += uppercase_letters
    if lower:
        all += lowercase_letters
    if nums:
        all += digits
    if symbols:
        all += symbols
    for x in range(amount):
        password = "".join(random.sample(all, length))
        print(password)
def lower_nums_symbols():
    uppercase_letters = "ABCDEFGHIJKLMNOPRSTUVYZQW"
    lowercase_letters = uppercase_letters.lower()
    digits = "0123456789"
    symbols = "!'^#+$%&/{([)]=}?\\*-_,;`´<>|"
    length = int(input("What Is The Length Of Password:"))
    amount = int(input("How Much Password?:"))
    upper, lower, nums, syms = False, True, True, True

    all = ""

    if upper:
        all += uppercase_letters
    if lower:
        all += lowercase_letters
    if nums:
        all += digits
    if syms:
        all += (symbols)
    for x in range(amount):
        password = "".join(random.sample(all, length))
        print(password)

