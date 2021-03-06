import re

def rearrange_name(name):
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])

if __name__ == "__main__":
    print(rearrange_name("Yigit, A. Uygur"))