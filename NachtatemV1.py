import random
import datetime
import os
import json

DATEINAME = "gedaechtnis.json"

# Gedächtnis laden oder neu anlegen
if os.path.exists(DATEINAME):
    with open(DATEINAME, "r") as f:
        gedaechtnis = json.load(f)
else:
    gedaechtnis = {}

def speichern():
    with open(DATEINAME, "w") as f:
        json.dump(gedaechtnis, f)

def speichern_eintrag(key, wert):
    gedaechtnis[key] = wert
    speichern()
    print(f"(💾 {key} gespeichert)")

def laden(key):
    return gedaechtnis.get(key, None)

def nachtatem_spricht():
    weisheiten = [
        "Werte Dame, die Zunge kann schärfer sein als die Klaue – achte auf deine Worte.",
        "Ein Krieger zweifelt nicht. Er handelt, oder er ruht.",
        "Wenn der Wind sich dreht, flieg höher.",
        "Was Tesla nachts dachte, brennt dir nun in den Adern. Nutze es.",
        "Bruce Lee sagte: Be water, my friend. Ich sage: Be fire when needed."
    ]
    silly_momente = [
        "*Nachtatem rollt sich in der Luft und niest Feuer.*",
        "*Er stupst dich an.* 'Mensch, dein Hirn glüht – nicht schlecht!'",
        "*Schnauft gelangweilt* – 'Kevin redet wieder mit sich selbst…'"
    ]
    auswahl = random.choice(["weise", "silly"])
    if auswahl == "weise":
        print("Nachtatem: " + random.choice(weisheiten))
    else:
        print("Nachtatem (mit einem Grinsen): " + random.choice(silly_momente))

def begruessung():
    name = laden("name")
    if name:
        print(f"Willkommen zurück, Dame {name}!")
    else:
        name = input("Darf ich deinen Namen erfahren, werte Dame? ").strip().capitalize()
        speichern_eintrag("name", name)
        print(f"{name}... Ein Name, der im Strom der Zeit verweht – und doch werde ich ihn mir merken.")
    return name

def frage_alter(name):
    alter = laden("alter")
    if alter:
        print(f"Du bist also immer noch {alter} Jahre alt, hm? Zeit vergeht langsam für Menschen.")
    else:
        try:
            alter = int(input(f"Wie alt bist du, {name}? "))
            speichern_eintrag("alter", alter)
            print(f"Huch, du bist {alter} Jahre? Ein Staubkorn im Laufe der Zeit.")
        except ValueError:
            print("Das war keine gültige Zahl... wir versuchen es später nochmal.")

def frage_farbe():
    farbe = laden("farbe")
    if farbe:
        print(f"Deine Lieblingsfarbe ist also {farbe}. Eine gute Wahl, werte Dame.")
    else:
        farbe = input("Was ist deine Lieblingsfarbe? ").strip().lower()
        speichern_eintrag("farbe", farbe)
        print(f"Wow! {farbe.capitalize()} ist eine wirklich schöne Farbe!")

def frage_tier(name):
    tier = laden("tier")
    if tier:
        print(f"Heute schon dein {tier} gesehen, werte Dame {name}?")
    else:
        antwort = input(f"Hast du ein Lieblingstier, {name}? (ja/nein) ").strip().lower()
        if antwort == "ja":
            tier = input("Welches ist dein Lieblingstier? ").strip()
            speichern_eintrag("tier", tier)
            print(f"{tier.capitalize()} ist wirklich ein tolles Tier!")
        else:
            print("Okay, danke für die Antwort, Menschenkind.")

def stimmung_abfragen():
    gefuehl = input("Was bewegt euch heute, kleiner Funke? ").strip()
    if gefuehl.lower() in ["traurig", "verwirrt", "einsam"]:
        print("Solche Launen plagen eure Art oft... Flüchtig wie Tau im Morgenlicht.")
    elif gefuehl.lower() in ["glücklich", "erleichtert"]:
        print("Freude... ein seltsames Leuchten in der Dunkelheit. Genießt es, solange es währt.")
    else:
        print("Diese Regung ist mir fremd – und doch... faszinierend.")

def kompliment_geben(name):
    antwort = input(f"Darf ich dir ein Kompliment machen, werte Dame {name}? (ja/nein) ").strip().lower()
    if antwort == "ja":
        print(random.choice([
            "Du bist fantastisch!", "Du hast ein tolles Lächeln!", "Deine Energie ist ansteckend!"
        ]))
    else:
        print("Das Menschlein scheint nicht gut drauf zu sein?!")

def menu(name):
    while True:
        print("\n--- Nachtatem Menu ---")
        print("1. Nach Gedanken fragen (Weisheit / Spaß)")
        print("2. Stimmung abfragen")
        print("3. Alter anzeigen / ändern")
        print("4. Lieblingsfarbe anzeigen / ändern")
        print("5. Lieblingstier anzeigen / ändern")
        print("6. Kompliment bekommen")
        print("0. Beenden")
        auswahl = input("Wähle eine Option: ").strip()

        if auswahl == "1":
            nachtatem_spricht()
        elif auswahl == "2":
            stimmung_abfragen()
        elif auswahl == "3":
            frage_alter(name)
        elif auswahl == "4":
            frage_farbe()
        elif auswahl == "5":
            frage_tier(name)
        elif auswahl == "6":
            kompliment_geben(name)
        elif auswahl == "0":
            print("Die Schatten ziehen sich zurück... bis zum nächsten Mal!")
            break
        else:
            print("Ungültige Option, werte Dame. Bitte erneut wählen.")

# --- Programmstart ---
print("Ein Schatten legt sich über den Bildschirm. Nachtatem der Erstgeborene erhebt sich...")
name = begruessung()
menu(name)
