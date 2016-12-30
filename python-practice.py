"""You can use this class to represent how classy someone
or something is.
"Classy" is interchangable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!"""

class Classy(object):

    def __init__(self):
        self.items = []

    def addItem(self, item):
        self.items.append(item)
    
    def getClassiness(self):
        
        tophat_value = 2
        bowtie_value = 4
        monocle_value = 5
        
        n_tophat = self.items.count('tophat')
        n_bowtie = self.items.count('bowtie')
        n_monocle = self.items.count('monocle')
        
        
        total_classiness = n_tophat * tophat_value + \
                           n_bowtie * bowtie_value + \
                           n_monocle * monocle_value
        
        return total_classiness
    

# Test cases
me = Classy()

# Should be 0
print me.getClassiness()

me.addItem("tophat")
# Should be 2
print me.getClassiness()

me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
# Should be 11
print me.getClassiness()

me.addItem("bowtie")
# Should be 15
print me.getClassiness()
