import sqlite3 as sq

id = 5
name = 'Pentium G6950'
year = 2010
price = 87
arch = 'Westmere'
cores = 2
threads = 2
fab = 32
tdp = 73
img = 'Легендарный гиперпень'

m = 'Intel'

with sq.connect('main.db') as con:
    cur = con.cursor()

# string = f"INSERT INTO {m.lower()}(cpu_id, name, year, price, arch, cores, threads, fab, tdp, img) VALUES({int(id)}, '{name}', {int(year)}, {int(price)}, {arch}, {int(cores)}, {int(threads)}, {int(fab)}, {int(tdp)}, '{img}')"

    cur.execute(f"""INSERT INTO {m.lower()}(cpu_id, name, year, price, arch, cores, threads, fab, tdp, img)
VALUES({int(id)}, '{name}', {int(year)}, {int(price)}, '{arch}', {int(cores)}, {int(threads)}, {int(fab)}, {int(tdp)}, '{img}')""")

    con.commit()

    # cur.execute("""INSERT INTO amd VALUES (2, 'Ryzen 3 1200', 2018, 109, 'Zen', 4, 4, 14, 65, 'fkyjreiuo')""")

    # result = cur.execute("""SELECT * FROM amd""")
    #
    # print(*result)
    #
    # result = cur.execute("""SELECT * FROM intel""")
    #
    # print(*result)

