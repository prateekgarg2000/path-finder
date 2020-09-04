from grid import *
from main import *
import queue

def BFS_path(start,end,draw):
    temp=end.parent
    while start!=temp:
        temp.put_state(7)
        temp=temp.parent
        draw()

def BFS_algorithm(draw, grid, start, end):
    q = queue.Queue(maxsize = 0)
    q.put(start)
    while q.qsize()>0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        current_spot=q.get()
        for neighbor in current_spot.neighbors:
            if neighbor.get_state() == 2:
                end.parent=current_spot
                BFS_path(start,end,draw)
                draw()
                return True
            elif neighbor.get_state() == 0:
                neighbor.put_state(5)
                neighbor.parent = current_spot
                q.put(neighbor)
                draw()
        if current_spot!=start:
            current_spot.put_state(4)
        draw()
    return True


if __name__ == "__main__":
    main(WIDTH,50,"BFS")
