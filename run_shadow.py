#!/usr/bin/env -S python3 -B

from time import time
from common.tk_drawer import TkDrawer
from shadow.polyedr import Polyedr


tk = TkDrawer()
try:
    for name in ["ccc", "cube", "box", "king", "cow"]:
        print("=============================================================")
        print(f"Начало работы с полиэдром '{name}'")
        start_time = time()
        poly = Polyedr(f"data/{name}.geom")
        poly.draw(tk)
        delta_time = time() - start_time
        print(f"Изображение полиэдра '{name}' заняло {delta_time} сек.")
        print(f"сумма длин рёбер, оба из концов которых — «хорошие» точки равна: {poly.good_point_perimetr()}")
        input("Hit 'Return' to continue -> ")
except (EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
