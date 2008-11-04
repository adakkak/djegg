from multiprocessing import Process
from orbited import start

p = Process(target=start.main, args=())
p.start()

