macondoyellow = "\033[38;2;242;191;64m"
reset = "\033[0m"
line1 = "    ########                        "
line2 = "   ####    ###                      "
line3 = " ###         ###  #####             "
line4 = "###           ##  ## ### ######     "
line5 = "###    #####  #####   ####  ###     "
line6 = "###   ##  ###  ####   ###   ###     "
line7 = "###   #   ###  ###.  ####   ##      "
line8 = " ###     ###   ###  ## ##  ###      "
line9 = "  ########     ###  #   #  ##       "
line10 = "              ###  ## ## ###        "
line11 = "              ###  ####  ###        "
line12 = "             ####        ##         "
line13 = "             ###         ##.##      "
line14 = "                          ####      "

lines = [line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12, line13, line14]
print("")
for i, line in enumerate(lines):
    if i == 1:
        print(f"{macondoyellow}{line}{reset}simon@macondo")
    elif i == 2:
        print(f"{macondoyellow}{line}{reset}-----------------------")
    else:
        print(macondoyellow + line + reset)