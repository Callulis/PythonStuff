# Chris Allulis
# What does this program do?

def addExclamationPoint(name):
    if len(name) > 2:
        name = name[0:2] + "!" + name[2:]
    return name


def main():
    name = "ANDREW"
    print name
    name = addExclamationPoint(name)
    print name


if __name__ == "__main__":
    main()

