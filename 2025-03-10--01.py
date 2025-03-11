# Projekt na punkty
print("Kojarzysz ten park na pętli Ogrody?")
park_kojarzenie = input()
if park_kojarzenie == "tak" or park_kojarzenie == "Tak":
    print("Super! Słuchaj, tam się wydarzyła historia niesamowita.")
    print("Szło dwóch mężczyzn nie wiedząc że zamknięte i jeden z nich wpadł w słup.")
    print("wpisz \"haha\" jeśli śmieszne. albo wpisz \"nie\" jeśli nieśmieszne i nie należy tak się śmiać")
    park_smieszne = input()
    if park_smieszne == "haha":
        print("Zły wybór, sorki")
    elif park_smieszne == "nie":
        print("O, o to chodzi. Nie wolno się śmiać z takich rzeczy - co z tego że ktoś tam chodził?")
        print("To że jest zamknięty sprawia tylko że skok przez płot staje się bardziej kuszący.")
        print("A co jeśli by się coś tej osobie stało? \"Smutno\"?")
        park_krzywda = input()
        if park_krzywda == "Smutno" or park_krzywda == "smutno":
            print("No smutno, no. Dobrze że się zgadzamy.")
            print("A gdzie się wiezie ludzi którym się krzywda stała?")
            krzywda_destination = input()
            if krzywda_destination == "do szpitala" or krzywda_destination == "Do szpitala" or krzywda_destination == "szpital":
                print("No tak by to było... Poziom rozumowania dwa plus dobry.")
                print("Troszkę dużo indentacji w tym kodzie.. Jakie słowo-klucz można by wykorzystać aby sobie z tym poradzić?")
                pomocny_keyword = input()
                if pomocny_keyword == "keyword return" or pomocny_keyword == "return" or pomocny_keyword == "zwracanie":
                    print("Tak! Ale mi nie wolno.")
                    print("A tak korzystając z okazji, to Uprzejmie Przepraszam wszystkich którzy musieli to czytać za brak inwencji twórczej.")
                    print("Pozdrawiam serdecznie.")
                else:
                    print("Coś innego miałem na myśli..")
            elif krzywda_destination == "na komendę" or krzywda_destination == "Na komendę" or krzywda_destination == "policja":
                print("Kajdanki nie pomogą jak kolega sobie czółko stłukł...")
            else:
                print("Doprawdy, nie rozumiem..")
        else:
            print("Nie czaję..")
    else:
        print("Nie rozumiem..")
else:
    print("Szkoda.")
