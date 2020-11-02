def connect_db(series, flag):
    import sqlite3 as sq

    with sq.connect('main.db') as con:
        cur = con.cursor()

        result = cur.execute(f"""SELECT * FROM {flag.lower()} WHERE name LIKE '%{series}%'""").fetchall()

        con.commit()
        print(*result)
        print(flag.lower())
        return result

connect_db('Ryzen 5', 'AMD')