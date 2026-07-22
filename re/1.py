import re

text="I love python"
match_string=re.search("python",text)

print(match_string)  #match object
print("test1")
print(match_string.group()) # return mached string only
print("test2")
print(match_string.groups()) # it return tuple if multiple pattern or character enclosed by small bracket

print("test3")
print(re.match(r"I", text))      # beginning check,return object with index
print(re.search(r"love", text))     #search it, return object with index
print(re.fullmatch(r"python", text)) # whole string


"""
character classes 
----------------------------

pattern                   meaning
-------                   --------
.                         any character except new line
\d                        Digit(0-9)
\D                        Not digit
\w                        word(letter,digit , underscore)
\W                        not word
\s                        Whitespace
\S                        No whitespace
"""

# print(re.findall(r"\d", "Hello 1,2 5,23,5,6,")) #return all digit (0-9) in list of string
# print(re.findall(r"\D", "Hello 1,2 5,23,5,6,")) #return all character separated  in list except digit
# print(re.findall(r"\w", "Hello 1,2 5,23,5,6,")) # return all word(letter, digit , underscore)
# print(re.findall(r"\W", "Hello 1,2 5,23,5,6,")) #return comma and space or  return expect word
#
# print(re.findall(r"\s", "Hello 1,2 5,23,5,6,")) #return whitespace
# print(re.findall(r"\S", "Hello 1,2 5,23,5,6,")) #return all except whitespace
#


"""
Anchors
--------------

symbol              meaning
-------            ----------
^                  start of string
$                  end of string

"""

# check mobile number start with 977-9
print(re.fullmatch(r"^977-9\d{9}","977-9810327373"))


date_check="2026-02-22"
m=re.search(r"(\d{4})-(\d{2})-(\d{2})",date_check)
print(m.group(1),m.group(2),m.group(3)) # 2026 02 22



text = "Contact us: a@example.com or b@test.org"

emails = re.findall(
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
    text
)

text = "Python     Django      FastAPI"

clean = re.sub(r"\s+", " ", text) # REMOVE SPACE


text = "Python,Django;FastAPI|Flask"

parts = re.split(r"[,;|]", text) #split
phone_pattern = re.compile(r"^9\d{9}$")

phone_pattern.fullmatch("9841234567")
phone_pattern.fullmatch("9811111111")
# [A-Za-z0-9._%+-] This is called a character class.Match exactly ONE character from the following list.



# Dont use match() for full Match