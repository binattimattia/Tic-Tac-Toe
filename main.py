EMPTY = " "

def create_player(name: str, symbol: str, wins: int) -> dict:
    return {
        "name": name,
        "symbol": symbol,
        "wins": wins
    }


def inizializza_tabellone() -> list[list[str]]:
    """Crea e restituisce una matrice 3x3 vuota."""
    tabellone = []
    for _ in range(3):  # Corretto per creare una matrice 3x3
        tabellone.append([EMPTY] * 3)

    return tabellone


def mostra_tabellone(tabellone: list[list[str]]) -> None:
    """Stampa la griglia di gioco in modo leggibile."""
    for riga in tabellone:
        print("|".join(riga))


def gioca_turno(tabellone: list[list[str]], giocatore: str, player_dict: dict) -> None:
    """Gestisce l'input del giocatore e aggiorna il tabellone."""
    input_riga = int(input("Inserisci la riga (1 - 3):\n")) - 1
    input_colonna = int(input("Inserisci la colonna (1 - 3):\n")) - 1
    if not tabellone[input_riga][input_colonna] == EMPTY:
        while not tabellone[input_riga][input_colonna] == EMPTY:
            print("Posizione già occupata, scegli un'altra posizione.")
            input_riga = int(input("Inserisci la riga (1 - 3):\n")) - 1
            input_colonna = int(input("Inserisci la colonna (1 - 3):\n")) - 1
    else:
        tabellone[input_riga][input_colonna] = player_dict[giocatore]["symbol"]


def check_row(tabellone: list[list[str]], riga) -> bool:
    return tabellone[riga][0] == tabellone[riga][1] == tabellone[riga][2] == "X" or tabellone[riga][0] == tabellone[riga][1] == tabellone[riga][2] == "O"


#def check_column(tabellone: list[list[str]], colonna) -> bool:
    

def verifica_vittoria(tabellone: list[list[str]]) -> bool:
    """Verifica se c'è un vincitore e restituisce True in caso affermativo."""
    for colonna in range(3):  
        for riga in tabellone:
            print(tabellone[riga][colonna])

verifica_vittoria([["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]])


def aggiorna_punteggio(giocatori: dict, vincitore: str) -> None:
    """Aggiorna il punteggio del giocatore vincente."""
    pass


def partita(giocatori: dict) -> None:
    """Gestisce il flusso principale del gioco, alternando i turni e determinando il risultato finale."""
    pass


def main() -> None:
    """Gestisce la sfida al meglio dei tre e dichiara il vincitore finale."""
    # player 1
    name_player_1 = input("Inserisci il nome del primo giocatore:\n")
    symbol_player_1 = input("Inserisci il simbolo (X - O):\n").upper()
    player_1 = create_player(name_player_1, symbol_player_1, 0)
    # player 2
    name_player_2 = input("Inserisci il nome del secondo giocatore:\n")
    symbol_player_2 = "X" if symbol_player_1 == "O" else "O"
    player_2 = create_player(name_player_2, symbol_player_2, 0)

    pass

if __name__ == "__main__":
    main()
