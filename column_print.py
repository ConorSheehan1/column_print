def column_print(strings, page_width=32, tab_width=4):
    ncols = len(strings)
    #add space for tabs
    page_width -= (ncols - 1) * tab_width
    width = page_width // ncols

    # while there is data left to print
    while not all(s == "" for s in strings):
        for i, s in enumerate(strings):
            # go to a new line for each column
            if i == 0: print()
            # if the column data doesn't exist create it using appropraite space
            to_print = " " * width if s == "" else s[:width]
            # if the column data does exist but is too short, 
            # add space to keep printing uniform
            if len(to_print) < width: to_print += (" "*(width-len(to_print)))
            # add tab space to the right of every column except the last
            tab = "" if i==len(strings)-1 else " " *tab_width
            # remove printed data from list of strings 
            strings[i] = s[width:]
            print(to_print+tab, end="")
    print()
        
            
            
if __name__ == "__main__":
    n = int(input("num strings"))
    l = []
    for i in range(n):
        l.append(input("string {}". format(i)))
    print(l)
    column_print(l)
