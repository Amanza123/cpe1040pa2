if __name__ == '__main__':
    str = []
    def cap_join(str):
        str2 = " ".join(str).title()
        return str2
    str = ["calvin", "and", "hobbes", "are", "the", "first", "spacemen", "on", "mars."]

    print(cap_join(str))