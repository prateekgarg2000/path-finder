from DFS import *

def main(width,ROWS,algo):
    win = pygame.display.set_mode((WIDTH, WIDTH))
    grid = make_grid(ROWS, width)
    start = None
    end = None
    happend=False
    run = True
    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (happend and (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE or pygame.mouse.get_pressed()[0] or pygame.mouse.get_pressed()[2])):
                run = False
                continue

            if pygame.mouse.get_pressed()[0]: # LEFT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                if not start and spot != end:
                    start = spot
                    start.put_state(1)
                elif not end and spot != start:
                    end = spot
                    end.put_state(2)
                elif spot != end and spot != start:
                    spot.put_state(3)

            elif pygame.mouse.get_pressed()[2]: # RIGHT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                spot.put_state(0)
                if spot == start:
                    start = None
                elif spot == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)
                    happend=True
                    if algo == "DFS":
                        DFS_algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)
    pygame.quit()

if __name__=="__main__":
    main(WIDTH,50,"DFS")
