import sqlite3

def main():
    con = sqlite3.connect('words.db')
    cur = sqlite3.cursor(con)
if __name__ == "__main__":
    main()
