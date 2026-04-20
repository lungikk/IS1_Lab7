import random
import pygame

# Inițializarea bibliotecii pygame
pygame.init()

# Constante pentru dimensiunile ferestrei și ale grilei
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
GRID_SIZE = 10
CELL_SIZE = 50

def generate_random_color_grid():
    """
    Generează o matrice de 10x10 ce conține culori RGB generate aleatoriu.
    Fiecare culoare este un tuplu de forma (R, G, B).
    """
    grid = []
    for _ in range(GRID_SIZE):
        row = []
        for _ in range(GRID_SIZE):
            # Generăm valori RGB între 0 și 255
            random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            row.append(random_color)
        grid.append(row)
    return grid

def main():
    # Crearea ferestrei principale
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Procedural Color Grid (Regenerare la 5 secunde)")

    # Inițializarea primei grile cu culori
    color_grid = generate_random_color_grid()
    
    # Setarea unui timer care va declanșa un eveniment la fiecare 5 secunde (5000 milisecunde)
    REGENERATE_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(REGENERATE_EVENT, 5000)

    is_running = True

    # Bucla principală a programului
    while is_running:
        # Setăm fundalul la negru
        screen.fill((0, 0, 0))

        # Desenăm grila de culori
        for row_index in range(GRID_SIZE):
            for col_index in range(GRID_SIZE):
                # Calculăm coordonatele x și y pentru fiecare celulă
                x_pos = col_index * CELL_SIZE
                y_pos = row_index * CELL_SIZE
                
                # Extragem culoarea celulei curente
                cell_color = color_grid[row_index][col_index]
                
                # Desenăm dreptunghiul pe ecran
                pygame.draw.rect(screen, cell_color, (x_pos, y_pos, CELL_SIZE, CELL_SIZE))

        # Actualizăm ecranul pentru a afișa modificările
        pygame.display.flip()

        # Gestionarea evenimentelor
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Oprim programul dacă utilizatorul închide fereastra
                is_running = False
                
            elif event.type == pygame.KEYDOWN:
                # Funcționalitatea manuală: regenerare la apăsarea tastei SPACE
                if event.key == pygame.K_SPACE:
                    color_grid = generate_random_color_grid()
                    
            elif event.type == REGENERATE_EVENT:
                # Funcționalitatea automată: regenerare din 5 în 5 secunde
                color_grid = generate_random_color_grid()

    # Închidem pygame la finalizarea buclei
    pygame.quit()

# Punctul de intrare în program
if __name__ == "__main__":
    main()
