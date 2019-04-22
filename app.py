from matrix import Matrix

mtx = Matrix()

mtx.load_from_file("matrix_v2.json")

r = mtx.query("select * from people where social_history.words.lower <- damn!!")

for i in r:
    c = i.social_history
    for cc in c:
        print(cc)

