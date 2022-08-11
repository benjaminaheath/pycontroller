import controller as c
import _thread
import server

LED = c.PyController(0, 1, 2)
_thread.start_new_thread(LED.thread, ())

server.init_server()
