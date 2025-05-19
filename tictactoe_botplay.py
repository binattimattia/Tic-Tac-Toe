EMPTY = " "

def create_player(name: str, symbol: str, wins: int, is_bot: bool = False) -> dict:
    return {
        "name": name,
        "symbol": symbol,
        "wins": wins,
        "is_bot": is_bot
    }

def inizializza_tabellone() -> list[list[str]]:
    return [[EMPTY for _ in range(3)] for _ in range(3)]

def mostra_tabellone(tabellone: list[list[str]]) -> None:
    print("  1   2   3")
    for i, riga in enumerate(tabellone):
        print(f"{i + 1} {' | '.join(riga)}")

def mosse_possibili(tabellone: list[list[str]]) -> list[tuple[int, int]]:
    """
    Restituisce una list di tutte le posizioni libere sul tabellone.
    Ogni posizione è rappresentata come una tupla (riga, colonna).

    Args:
        tabellone (list[list[str]]): Il tabellone di gioco.

    Returns:
        list[tuple[int, int]]: Lista delle posizioni libere.
    """
    return [(r, c) for r in range(3) for c in range(3) if tabellone[r][c] == EMPTY]


def verifica_vittoria(tabellone: list[list[str]]) -> bool:
    for i in range(3):
        if tabellone[i][0] == tabellone[i][1] == tabellone[i][2] != EMPTY:
            return True
        if tabellone[0][i] == tabellone[1][i] == tabellone[2][i] != EMPTY:
            return True
    if tabellone[0][0] == tabellone[1][1] == tabellone[2][2] != EMPTY:
        return True
    if tabellone[0][2] == tabellone[1][1] == tabellone[2][0] != EMPTY:
        return True
    return False

def verifica_pareggio(tabellone: list[list[str]]) -> bool:
    for row in tabellone:
        for cell in row:
            if cell == EMPTY:
                return False  # C'è almeno una cella vuota, quindi non è un pareggio
    return True  # Tutte le celle sono occupate, è un pareggio

def aggiorna_punteggio(giocatore: dict) -> None:
    giocatore["wins"] += 1

def gioca_turno(tabellone: list[list[str]], giocatore: dict, avversario: dict) -> None:
    if giocatore["is_bot"]:
        print(f"{giocatore['name']} sta pensando...")
        r, c = mossa_migliore(tabellone, giocatore["symbol"], avversario["symbol"])
        tabellone[r][c] = giocatore["symbol"]
    else:
        while True:
            try:
                input_riga = int(input(f"{giocatore['name']} ({giocatore['symbol']}), inserisci la riga (1-3): ")) - 1
                input_colonna = int(input(f"{giocatore['name']} ({giocatore['symbol']}), inserisci la colonna (1-3): ")) - 1
                if tabellone[input_riga][input_colonna] == EMPTY:
                    tabellone[input_riga][input_colonna] = giocatore["symbol"]
                    break
                else:
                    print("Posizione già occupata, scegli un'altra.")
            except (ValueError, IndexError):
                print("Input non valido. Inserisci numeri tra 1 e 3.")

def minimax(tabellone: list[list[str]], depth: int, is_maximizing: bool, bot_symbol: str, player_symbol: str) -> int:
    """
    Implementa l'algoritmo Minimax per determinare il punteggio ottimale di una mossa.
    Simula tutte le possibili mosse future per il bot e il giocatore.

    Args:
        tabellone (list[list[str]]): Il tabellone di gioco.
        depth (int): La profondità della ricorsione.
        is_maximizing (bool): Indica se il bot sta massimizzando il punteggio.
        bot_symbol (str): Il simbolo del bot (X o O).
        player_symbol (str): Il simbolo del giocatore umano (X o O).

    Returns:
        int: Il punteggio della mossa (1 per vittoria del bot, -1 per vittoria del giocatore, 0 per pareggio).
    """
    # Controlla se c'è una vittoria o un pareggio
    if verifica_vittoria(tabellone):
        return 1 if not is_maximizing else -1
    if verifica_pareggio(tabellone):
        return 0

    if is_maximizing:
        # Il bot cerca di massimizzare il punteggio
        best_score = -float("inf")
        for r, c in mosse_possibili(tabellone):
            tabellone[r][c] = bot_symbol  # Simula la mossa del bot
            score = minimax(tabellone, depth + 1, False, bot_symbol, player_symbol)
            tabellone[r][c] = EMPTY  # Ripristina lo stato del tabellone
            best_score = max(score, best_score)
        return best_score
    else:
        # Il giocatore cerca di minimizzare il punteggio
        best_score = float("inf")
        for r, c in mosse_possibili(tabellone):
            tabellone[r][c] = player_symbol  # Simula la mossa del giocatore
            score = minimax(tabellone, depth + 1, True, bot_symbol, player_symbol)
            tabellone[r][c] = EMPTY  # Ripristina lo stato del tabellone
            best_score = min(score, best_score)
        return best_score


def mossa_migliore(tabellone: list[list[str]], bot_symbol: str, player_symbol: str) -> tuple[int, int]:
    """
    Determina la mossa migliore per il bot utilizzando l'algoritmo Minimax.

    Args:
        tabellone (list[list[str]]): Il tabellone di gioco.
        bot_symbol (str): Il simbolo del bot (X o O).
        player_symbol (str): Il simbolo del giocatore umano (X o O).

    Returns:
        tuple[int, int]: La posizione (riga, colonna) della mossa migliore.
    """
    best_score = -float("inf")  # Inizializza il miglior punteggio possibile
    best_move = None  # Inizializza la mossa migliore

    for r, c in mosse_possibili(tabellone):
        tabellone[r][c] = bot_symbol  # Simula la mossa del bot
        score = minimax(tabellone, 0, False, bot_symbol, player_symbol)  # Calcola il punteggio della mossa
        tabellone[r][c] = EMPTY  # Ripristina lo stato del tabellone
        if score > best_score:
            best_score = score  # Aggiorna il miglior punteggio
            best_move = (r, c)  # Aggiorna la mossa migliore

    return best_move

def partita(giocatori: list[dict]) -> dict:
    tabellone = inizializza_tabellone()
    turno = 0
    while True:
        mostra_tabellone(tabellone)
        giocatore_corrente = giocatori[turno % 2]
        avversario = giocatori[(turno + 1) % 2]
        gioca_turno(tabellone, giocatore_corrente, avversario)
        if verifica_vittoria(tabellone):
            mostra_tabellone(tabellone)
            print(f"{giocatore_corrente['name']} ha vinto la partita!")
            aggiorna_punteggio(giocatore_corrente)
            return giocatore_corrente
        if verifica_pareggio(tabellone):
            mostra_tabellone(tabellone)
            print("La partita è finita in pareggio!")
            return None
        turno += 1

def main() -> None:
    name_player = input("Inserisci il tuo nome: ")
    symbol_player = input("Vuoi essere X o O? ").upper()
    while symbol_player not in ["X", "O"]:
        symbol_player = input("Simbolo non valido. Inserisci X o O: ").upper()

    symbol_bot = "O" if symbol_player == "X" else "X"

    player = create_player(name_player, symbol_player, 0)
    bot = create_player("Bot", symbol_bot, 0, is_bot=True)

    giocatori = [player, bot] if player["symbol"] == "X" else [bot, player]

    while player["wins"] < 2 and bot["wins"] < 2:
        vincitore = partita(giocatori)
        if vincitore:
            print(f"Punteggio: {player['name']} {player['wins']} - Bot {bot['wins']}")

    if player["wins"] == 2:
        print(f"{player['name']} ha vinto la sfida!")
    else:
        print("Il Bot ha vinto la sfida!")

if __name__ == "__main__":
    main()
