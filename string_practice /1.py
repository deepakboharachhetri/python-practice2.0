
# --------------string strip() methods---------------------------------
# syntax string.strip(string_to_be_remove),string.lstrip(string_to_be_remove),string.lstrip(string_to_be_remove)

string_example1=" Hello ! Hari, What's up ?Are you fine dude? "
print(string_example1.strip()) #by default it remove space from left and right
print(string_example1.lstrip()) # it removes left space present before first character
print(string_example1.rstrip()) # it removes right space present after last character

string_example2="hello dude"
print(string_example2.strip("he"))  #it removes h and e  if  they exist in first, end of the string (even
# space present may affect the strip means if space present before(beginning) or after(last) the letters(h,e) it will not work

print(string_example2.lstrip("hello")) #it removes the characters where beginning of letters matches
print(string_example2.rstrip("dude")) #it removes the characters where last of letters matches


# ------------string replace() method-----------------------
# syntax : string.replace(old,new,count)  , by default  count = count of old
print("replace without count",string_example2.replace("d","j"))
print("replace with count",string_example2.replace("d","j",1))



# -----------------string slicing-------------------------
# syntax : string[start:stop:step], start starts with 0 and stop check condition index<stop

print("string slicing (only changing start)", string_example2[2:])
print("string slicing (only changing stop", string_example2[:2])
print("string slicing (only changing step)", string_example2[::2])
print("string slicing", string_example2[1:4:2])

string_example3=string_example2[:] # for shallow copy
print("string_example2_id,string_example3_id",id(string_example2),id(string_example3)) # same id no problem because immutable,
# from the same id we also demonestrate interning or cachinging in python



# ------join()-----------------
# syntax: seperator.join(iterable)
l=["hello","brother","whatsapp","!"]
print(" ".join(l))
print("_".join(l))


# -------------split()-------------
# syntax: string.split(character,maxsplit) , by default character is space and max_split =all
print("split",string_example1.split())
print("split",string_example1.split("l")) #split character not include in list after split
print("split",string_example1.split("l",1)) #lsplit maxsplit 1
print("split",string_example1.rsplit("l",1)) #rsplit maxsplit 2


# ------------partition()-------
# syntax :string.partition(char) , output exactly 3 member :before  char, char, after char
print("partition",string_example1.partition("l"))
print("partition",string_example1.rpartition("l"))

# -----count,startswith(),endswith()-----------

print("count",string_example1.count("e"))
path=r"home/hello.pdf"
print("startswith",path.startswith("home"))
print("count",path.endswith(".pdf"))


# ---------center(),ljust(), rjust(), zfill()-----------
# syntax :string.center(width,fillchar) same  for ljust and rjust, fillchar by default space
# syntax : string.zfill(width)
test_justify="hello brother"
print(test_justify.center(50))
print(test_justify.center(50,"1"))
print(test_justify.ljust(50,"1"))
print(test_justify.rjust(50,"1"))
print(test_justify.zfill(50)) #it justify using 0 only for rjustify
print("1".zfill(5))
