EMPTY = " "

def create_player(name: str, symbol: str, wins: int) -> dict:
    return {
        "name": name,
        "symbol": symbol,
        "wins": wins
    }

def inizializza_tabellone() -> list[list[str]]:
    """Crea e restituisce una matrice 3x3 vuota."""
    return [[EMPTY for _ in range(3)] for _ in range(3)]

def mostra_tabellone(tabellone: list[list[str]]) -> None:
    """Stampa la griglia di gioco in modo leggibile."""
    print("  1   2   3")
    index = 0
    for riga in tabellone:
        print(f"{index + 1} ", end="")
        print(" | ".join(riga))
        index += 1


def gioca_turno(tabellone: list[list[str]], giocatore: dict) -> None:
    """Gestisce l'input del giocatore e aggiorna il tabellone."""
    while True:
        try:
            input_riga = int(input(f"{giocatore['name']} ({giocatore['symbol']}), inserisci la riga (1-3): ")) - 1
            input_colonna = int(input(f"{giocatore['name']} ({giocatore['symbol']}), inserisci la colonna (1-3): ")) - 1
            if tabellone[input_riga][input_colonna] == EMPTY:
                tabellone[input_riga][input_colonna] = giocatore["symbol"]
                break
            else:
                print("Posizione già occupata, scegli un'altra posizione.")
        except (ValueError, IndexError):
            print("Input non valido. Inserisci un numero tra 1 e 3.")

def verifica_vittoria(tabellone: list[list[str]]) -> bool:
    """Verifica se c'è un vincitore."""
    # Controlla righe e colonne
    for i in range(3):
        if tabellone[i][0] == tabellone[i][1] == tabellone[i][2] != EMPTY:
            return True
        if tabellone[0][i] == tabellone[1][i] == tabellone[2][i] != EMPTY:
            return True
    # Controlla diagonali
    if tabellone[0][0] == tabellone[1][1] == tabellone[2][2] != EMPTY:
        return True
    if tabellone[0][2] == tabellone[1][1] == tabellone[2][0] != EMPTY:
        return True
    return False

def verifica_pareggio(tabellone: list[list[str]]) -> bool:
    """Verifica se la partita è in pareggio."""
    for riga in tabellone:
        if EMPTY in riga:
            return False
    return True

def aggiorna_punteggio(giocatore: dict) -> None:
    """Aggiorna il punteggio del giocatore vincente."""
    giocatore["wins"] += 1

def partita(giocatori: list[dict]) -> dict:
    """Gestisce il flusso principale del gioco."""
    tabellone = inizializza_tabellone()
    turno = 0
    while True:
        mostra_tabellone(tabellone)
        giocatore_corrente = giocatori[turno % 2]
        gioca_turno(tabellone, giocatore_corrente)
        if verifica_vittoria(tabellone):
            mostra_tabellone(tabellone)
            print(f"{giocatore_corrente['name']} ha vinto la partita!")
            aggiorna_punteggio(giocatore_corrente)
            return giocatore_corrente
        if verifica_pareggio(tabellone):
            mostra_tabellone(tabellone)
            print("La partita è terminata in pareggio!")
            return None
        turno += 1

def main() -> None:
    """Gestisce la sfida al meglio dei tre e dichiara il vincitore finale."""
    # Inizializza i giocatori
    name_player_1 = input("Inserisci il nome del primo giocatore: ")
    symbol_player_1 = input("Inserisci il simbolo (X o O): ").upper()
    while symbol_player_1 not in ["X", "O"]:
        symbol_player_1 = input("Simbolo non valido. Inserisci X o O: ").upper()
    player_1 = create_player(name_player_1, symbol_player_1, 0)

    name_player_2 = input("Inserisci il nome del secondo giocatore: ")
    symbol_player_2 = "O" if symbol_player_1 == "X" else "X"
    player_2 = create_player(name_player_2, symbol_player_2, 0)

    giocatori = [player_1, player_2]

    # Sfida al meglio dei tre
    while player_1["wins"] < 2 and player_2["wins"] < 2:
        vincitore = partita(giocatori)
        if vincitore:
            print(f"Punteggio: {player_1['name']} {player_1['wins']} - {player_2['name']} {player_2['wins']}")

    # Dichiarazione del vincitore finale
    if player_1["wins"] == 2:
        print(f"{player_1['name']} è il vincitore della sfida!")
    else:
        print(f"{player_2['name']} è il vincitore della sfida!")

if __name__ == "__main__":
    main()