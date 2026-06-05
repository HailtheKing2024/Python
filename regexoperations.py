import re

text_to_search = """
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreymms.com

321-555-4321
123.555.1234
123*555*1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat
"""

sentence = "Start a sentence and then bring it to an end"

pattern = re.compile(r"Mr\.?\s[A-Z]\w*")

matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)
