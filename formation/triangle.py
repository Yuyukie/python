cote_a = float(input ("Renseignez la longeur du cote A"))
cote_b = float(input ("Renseignez la longeur du cote B"))
cote_c = float(input ("Renseignez la longeur du cote C"))

if cote_a == cote_b == cote_c :
    print ("triangle équilatéral")
elif cote_a == cote_b or cote_a == cote_c or cote_b == cote_c :
    print ("triangle isocele")
else :
    print("triangle quelconque")
    