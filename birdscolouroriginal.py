# ----------------------------Bird Sort 2 - Color Puzzle----------------------------------------------------------------------
# Nenhuma biblioteca foi usada para o c√≥digo. 
# O cÛdigo ser· elaborado em inglÍs/portuguÍs, os coment·°rios e as erros likewise
# N„o usamos nenhuma biblioteca externa como pygame e numlib neste c√≥digo porque o jogo utiliza apenas os recursos internos do Python para garantir uma simplicidade e nenhuma depend√™ncia extra like (bibliotecas).
# O cÛdigo utiliza apenas funcionalidades internas do Python tipo como listas, loops e conditionals para implementar a lÛgica do jogo.
# Um jogo de paci√™ncia para um jogador onde o objetivo √© organizar as cores em frascos separados.
# Flask significa um recipiente ou garrafa, normalmente usado para armazenar lÌquidos. 
# Neste jogo, os frascos s√£o usados para armazenar cores. 
# O jogo È jogado com 6 frascos, onde cada frasco pode conter ent„o 4 cores.

def check_victory(self):
    """
    Check if any flask is completely filled with the same color.
    If so, print 'VICTORY' and return True.
    """
    for flask in self.flasks:
        if len(flask) == 4 and len(set(flask)) == 1:
            print("VICTORY")
            return True
    return False

class BirdSortGame:
    def __init__(self, flasks):
        """
        Initialize the game with the given flasks.
        Each flask is represented as a list of colors (strings)/ 
        Iniciarei o jogo com frascos dados, na qual 
        cada frasco √© representado com o uma lista de cores diferentes(strings).
        """
        self.flasks = flasks

    def display_flasks(self):
        """Disp√¥e o estado actual do frasco(flask)."""
        print("\nCurrent Flasks:")
        for i, flask in enumerate(self.flasks):
            print(f"Flask {i + 1}: {flask}")
        print()

    def is_valid_move(self, from_flask, to_flask):
        """
        Check if moving the top color from one flask to another is valid.
        A move is valid if:
        - The source flask is not empty.
        - The destination flask is not full.
        - The top color of the source flask matches the top color of the destination flask (or the destination is empty)/
        Verifica se a primeira cor (sentido come√ßando da direita para esquerda) pode mover para um outro frasco que est√° v√°lido. 
        O movimento ser· v·lido se: 
        - O frasco principal n„o estiver vazio. 
        - O destino do frasco no √© vazio. 
        - A primeira cor do frasco principal tem que combinar com a primeira do frasco destino(ou o destina√ß√£o √© vazia).
        """
        if not self.flasks[from_flask]:
            return False
        if len(self.flasks[to_flask]) >= 4:  # Aqui assumo que cada frasco consegue apenas manter 4 cores
            return False
        if not self.flasks[to_flask] or self.flasks[from_flask][-1] == self.flasks[to_flask][-1]:
            return True
        return False

    def make_move(self, from_flask, to_flask):
        """
        Perform the move by transferring the top color from one flask to another.
        Assumes the move is valid/ 
        Completa um movimento por transferir a primeira cor de um frasco para outro. 
        Assume que o movimento √© v√°lido.
        """
        color = self.flasks[from_flask].pop()
        self.flasks[to_flask].append(color)

    def is_solved(self):
        """
        Check if the game is solved.
        The game is solved if each flask is either empty or contains only one color.
        Verifica-se se o jogo j√° terminou. 
        O jogo apenas temina quando cada frasco ou est√° vazia(tecnicamente) ou cont√©m apenas uma sequ√™ncia de 4 cores.
        """
        for flask in self.flasks:
            if len(flask) > 0 and len(set(flask)) > 1:
                return False
        return True

    def play(self):
        """Main game loop for a human player. 
           Criando uma classe que efectuar√° um loop para as possibilidades do jogabilidade do user/"""
        print("Welcome to Bird Sort 2 - Color Puzzle!")
        self.display_flasks()

        while not self.is_solved():
            try:
                # Pedirei para o user efectuar um movimento de 1-6(flasks)
                from_flask = int(input("Move from flask (1-6): ")) - 1
                to_flask = int(input("Move to flask (1-6): ")) - 1

                # Validarei o movimento de cada cor para cada frasco 
                if self.is_valid_move(from_flask, to_flask):
                    self.make_move(from_flask, to_flask)
                else:
                    print("Invalid move. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter numbers between 1 and 6.")

            # Vou dispor cada frasco actualizado
            self.display_flasks()

        print("Congratulations! You solved the puzzle!")


# Exemplificando ser√£o 6 frascos e apenas 2 frascos estar√£o, inicialmente, vazios. 

initial_flasks = [
    ["red", "blue", "red", "blue"],  #  Frasco 1
    ["green", "yellow", "green", "yellow"],  # Flask 2/ Frasco 2
    ["blue", "red", "yellow", "green"],  # Flask 3 / Frasco 2
    ["yellow", "green", "blue", "red"],  # Flask 4 / Frasco 4
    [],  # Frasco 5 (vazio) /Flask 5 (empty)
    []   # Frasco 5 (vazio) /Flask 6 (empty)
]


game = BirdSortGame(initial_flasks)
game.play()