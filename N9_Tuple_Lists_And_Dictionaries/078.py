TV_programmes = ["Uzbekistan_24", "Yoshlar", "Dunyo_boylab", "Ruxsor"]

for TV_programm in TV_programmes:
    print(TV_programm)
New_TV_Programm = input("Enter a name new TV programm: \n")
Position_TV_Programm = int(input("Enter a position: \n"))
TV_programmes.insert(Position_TV_Programm, New_TV_Programm)

for TV_programm in TV_programmes:
    print(TV_programm)