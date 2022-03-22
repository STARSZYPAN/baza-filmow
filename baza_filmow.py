

def menu():
    print("   MENU BIBLIOTEKI FOLMOW I SERIALI  ")
    print("---Wpisz w konsoli wybraną komendę---")
    print()
    print("Co chcesz zrobić?")
    print()
    print("LISTA FILMÓW-wyswietl listę filmów")
    print("LISTA SERIALI-wyswietl listę seriali")
    print("DODAJ FILM-dodaj film do bazy")
    print("DODAJ SERIAL-dodaj seril do bazy")
    print("SZUKAJ FILMU-znajdź film (po roku wydania)")
    print("SZUKAJ SERIALI-znadź serial (po roku wydania)")
    print("EXIT- wyjscie z programu")



def film(lista_filmów):
    if len(lista_filmów)==0:
        print("Brak Filmów do wyświetlenia.\n")
        return
    else:
        i=1
        for film in lista_filmów:
            rząd=film
            print(str(i) + "." + (rząd [0])
                + " - " + str(rząd[1]) + "-" +  str(rząd[2]))
            i +=1
        print()

def serial(lista_seriali):
    if len(lista_seriali)==0:
        print("Brak seriali do wyświetlenia.\n")
        return
    else:
        i=1
        for serial in lista_seriali:
            rząd_1=serial
            print(str(i) + "." + (rząd_1[0])
                + " - " + str(rząd_1[1]) + "-" +  str(rząd_1[2]) + " S"+ str(rząd_1[3]) + " E" + str(rząd_1[4]))
            i +=1
        print()

def dodaj_film(lista_filmów):
    tytuł= input("Tytuł: ") 
    rok_prod=int(input("Rok produkcji: "))
    gatunek=input("Gatunek: ")
    film=[]
    film.append(tytuł)
    film.append(rok_prod)
    film.append(gatunek)
    lista_filmów.append(film)
    print(film[0] + "  zostal dodany.\n")

def dodaj_serial(lista_seriali):
    tytuł= input("Tytuł: ") 
    rok_prod=int(input("Rok produkcji: "))
    gatunek=input("Gatunek: ")
    sezon=int(input("Sezon: "))
    odcinek=int(input("Odcinek: "))
    serial=[]
    serial.append(tytuł)
    serial.append(rok_prod)
    serial.append(gatunek)
    serial.append(sezon)
    serial.append(odcinek)
    lista_seriali.append(film)
    print(serial[0] + "  zostal dodany.\n")

def znajdź_film(lista_filmów):
    rok_prod=int(input("Podaj rok produkcji szukanego filmu: "))  
    for film in lista_filmów:
        if film[1]==rok_prod:
            print(film[0])

def znajdź_serial(lista_seriali):
    rok_prod=int(input("Podaj rok produkcji szukanego serialu: "))  
    for serial in lista_seriali:
        if serial[1]==rok_prod:
            print(str(serial[0]))

def main():
    lista_filmów=[["Venom 2", 2021 ,"Sci-fi"],["Project Adam",2022,"Sci-fi"],["Matrix:Rezurekcje",2022,"Sci-fi"],["Monthy Python i Święty Grall",1975,"Komedia"]]
    lista_seriali=[["Peaky Blinder's",2019,"Sensacyjny" ,1,2],["Vikings",2018,"Przygodowy",2,3]]

    menu()
    while True:
        print()
        czynność= input("Podaj komendę: ")
        if czynność== "lista filmów":
            film(lista_filmów)
        elif czynność=="lista seriali":
            serial(lista_seriali)
        elif czynność== "dodaj film":
            dodaj_film(lista_filmów)
        elif czynność== "dodaj serial":
            dodaj_serial(lista_seriali)
        elif czynność== "szukaj filmu":
            znajdź_film(lista_filmów )
        elif czynność== "szukaj seriali":
            znajdź_serial(lista_seriali)
        elif czynność=="exit":
            break
            
        else:
            print("Niepoprawna komenda,prosze powtórz. \n")
            
if __name__=="__main__":
    main()


    