from matplotlib.pyplot import connect
from soccer_player import Soccer_player
import sqlite3


def main():
    son = Soccer_player("son","Korea", "Tottenham", "31", "183", "FW", "30000")
    son.save_db()
    

main()