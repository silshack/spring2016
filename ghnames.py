# I ran this script with `python ghnames.py` until it was correct then
# ran `python ghnames.py >> _config.yml` to add it its output to the
# end of our _config.yml.

# In Python """ starts a string that can span multiple lines
names = """jamesma560
tsukori
jwarrich
pmr1027
JayYang95
namagic
EternalFootman
ericabrody
gao14g
RhymesWithMecca
hannahlwang
ShyArmadillo8
touchwick
payalpn
clairewlj
wfh1972
tyym0215
yiyangshi
nataliele"""


# The data format our blog uses is called YAML.  It's a common way of
# getting simple data into a program that processes text.
for name in sorted(names.split("\n"), key=str.lower): # the .split() method makes a list out of a string, split at a character. The sorted() function alphabetizes them. 
    print """  {0}:                    
    name: {0}
    prof: false
    gravatar:
    website: 
    github: {0}
    twitter: 
    about: "Here's a little about {0}"
    """.format(name)   # The format method inserts the nth argument at {n} (starting with the zeroth)