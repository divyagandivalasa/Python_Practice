tabby_cat = "\t I'm tabbed in"
persian_cat = "I'm split \non a line"
backslash_cat = "I'm \\ a \\ cat"
fat_cat = '''
I'll do a list
\t* Cat Food
\t* Fishes
\t* Catnip\n\t* Grass
'''
escape_seq = "Divya\'s"

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print "%s" % escape_seq
