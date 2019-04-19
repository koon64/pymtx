from matrix import Matrix

mtx = Matrix()

mtx.load_from_file("matrix_v2.json")

r = mtx.query("select * from people where address.lower.words <- autumn")
for i in r:
    print(i)

