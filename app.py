from matrix import Matrix

mtx = Matrix()

mtx.load_from_file("matrix_v2.json")

me = mtx.name_match("max a")

print(me.biography)