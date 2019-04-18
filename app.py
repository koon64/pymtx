from matrix import Matrix

mtx = Matrix()

mtx.load_from_file("matrix_v2.json")

r = mtx.query("select * from people where grade == 9")
for i in r:
    print(i)

