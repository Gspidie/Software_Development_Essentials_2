RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[33m'
RESET = '\033[0m'

list = "a b "

def testFunc():
    global list 

    list += f"{GREEN}a{RESET} "

testFunc()

print(list)