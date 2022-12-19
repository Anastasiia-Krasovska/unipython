spielfeld = list(range(1,10))

def zeichnen_tafel(spielfeld):
    print ("-" * 13)
    for i in range(3):
        print ("|", spielfeld[0+i*3], "|", spielfeld[1+i*3], "|", spielfeld[2+i*3], "|")
        print ("-" * 13)

def take_input(spieler_token):
    valid = False
    while not valid:
        spieler_antwort = input("Ihr Zug  " + spieler_token+"? ")
        try:
            spieler_antwort = int(spieler_antwort)
        except:
            print ("Falsche Eingabe. Sind Sie sicher, dass Sie eine Nummer eingegeben haben?")
            continue
        if spieler_antwort >= 1 and spieler_antwort <= 9:
            if (str(spielfeld[spieler_antwort-1]) not in "XO"):
                spielfeld[spieler_antwort-1] = spieler_token
                valid = True
            else:
                print ("Diese Zelle ist bereits eingenommen")
        else:
            print ("Falsche Eingabe. Geben Sie eine Zahl von 1 bis 9 ein.")

def prüf_gewinnen(spielfeld):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if spielfeld[each[0]] == spielfeld[each[1]] == spielfeld[each[2]]:
            return spielfeld[each[0]]
    return False

def main(spielfeld):
    zähler = 0
    sieg = False
    while not sieg:
        zeichnen_tafel(spielfeld)
        if zähler % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        zähler += 1
        if zähler > 4:
            tmp = prüf_gewinnen(spielfeld)
            if tmp:
                print (tmp, "gewonnen!")
                sieg = True
                break
        if zähler == 9:
            print ("Gleichstand!")
            break
    zeichnen_tafel(spielfeld)

main(spielfeld)