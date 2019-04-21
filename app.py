from matrix import Matrix

mtx = Matrix()

mtx.load_from_file("matrix_v2.json")

me = mtx.simple_search("max walk")[0]

sh = []

for n in sh:
    if n.node_type == "post":
        print(n)
        for c in n.comments:
            print(c)
        for t in n.tags:
            print(t)
        for l in n.likes:
            print(l)
        print()

    elif n.node_type == 'video':
        print(n)