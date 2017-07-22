def column_print(strings, max_len=32):
    ncols = len(strings)
    #add space for tabs
    max_len -= (ncols-1)*4
    width = max_len//ncols

    while strings:
        for i, s in enumerate(strings):
            if i==0:
                print()
            to_print = " "*width if s=="" else s[:width]
            if len(to_print) < width:
                to_print+=(" "*(width-len(to_print)))
            tab = "" if i==len(strings)-1 else " " *4
            strings[i] = s[width:]
            print(to_print+tab, end="")
        if all(s=="" for s in strings):
            break
    print()
        
            
            
if __name__ == "__main__":
    n = int(input("num strings"))
    l = []
    for i in range(n):
        l.append(input("string {}". format(i)))
    print(l)
    column_print(l)
