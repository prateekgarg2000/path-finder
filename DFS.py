from grid import *
from main import *

def DFS_path(start,end,draw):
    temp=end.parent
    while start!=temp:
        temp.put_state(7)
        temp=temp.parent
        draw()

def DFS_algorithm(draw, grid, start, end):
    stack = []
    stack.append(start)
    # current_path.append(start)
    while len(stack) > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        should_pop=True
        current_spot=stack[-1]
        for neighbor in current_spot.neighbors:
            if neighbor.get_state()==2:
                end.parent=current_spot
                DFS_path(start,end,draw)
                draw()
                return True

            elif neighbor.get_state()==0:
                neighbor.put_state(5)
                should_pop=False
                neighbor.parent=current_spot
                stack.append(neighbor)
                draw()
        stack[-1].put_state(4)
        if(should_pop):
            stack.pop()
        draw()
    return True

if __name__ == "__main__":
    main(WIDTH,30,"DFS")
