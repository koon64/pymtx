from matrix import Matrix

mtx = Matrix()

mtx.load_from_file("matrix_v2.json")

r = mtx.query("select * from people where name* == max")
for i in r:
    print(i)

# me = mtx.search("max a")[0]
# y = me.school_years[0]
# sem = y.semesters[1]
# sch = sem.schedule
# rot = sch.rotations[1]
# for cl in rot.classes:
#
#     print(cl.name if not cl.is_free else "free")
