import pygame as pg
import random
pg.init()

rows,cols = (5,5)
choice = [0,0,0,0,0,0,1]
arr = [[0]*cols]*rows
arr = [[random.choice(choice) for j in range(len(arr))] for i in range(len(arr))]



print(arr)


# screen = pg.display.set_mode((600,800))
# running = True




# while running==True:
#     pg.display.flip()
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
            # running = False