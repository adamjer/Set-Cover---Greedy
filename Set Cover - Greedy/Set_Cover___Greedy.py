import sys
 
class Logger(object):
    def __init__(self):
        self.log_destination = [sys.stdout]
 
    def add_log_file(self, filename):
        self.log_destination.append(open(filename, "a"))
 
    def write(self, message):
        for item in self.log_destination:
            item.write(message)
 
    def flush(self):
        for item in self.log_destination:
            item.flush()

def replaceMultiple(mainString, toBeReplaces, newString):
    # Iterate over the strings to be replaced
    for elem in toBeReplaces :
        # Check if string is in the main string
        if elem in mainString :
            # Replace the string
            mainString = mainString.replace(elem, newString)    
    return  mainString


def createUniverse():
    print("Create universe. Format {a, b, c, ..., x, y, z}.")
    line = input()
    return set(createSet(line))

def createSets():
    print("Create sets. Format {a, b, c, ..., x, y, z}. Until empty input.")
    sets = set()
    while True:
        line = input()
        if not line:
            break
        sets.add(frozenset(createSet(line)))

    return sets

def createSet(line):    
    line = replaceMultiple(line, ['{', '}', ' '], "")
    return line.split(',')

def setCover(universe, subSets):
    elements = set(e for s in subSets for e in s)
    
    if elements != universe:
        return None

    covered = set()
    cover = []

    while covered != elements:
        subSet = max(subSets, key=lambda s: len(s - covered))
        cover.append(subSet)
        covered |= subSet

    return cover


sys.stdout = Logger()
sys.stdout.add_log_file("test.log")

universe = createUniverse()
subSets = createSets()
results = setCover(universe, subSets)

print("Results:")
for s in results:
    result = "{"
    for e in s:
        result += e + ", "
    print(result[:-2] + "}")