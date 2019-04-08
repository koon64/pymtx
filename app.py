from matrix import Matrix

mtx = Matrix()

mtx.load_from_file("matrix_v2.json")

me = mtx.search("max a")[0]

print(me.groups)
