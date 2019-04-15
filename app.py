from matrix import Matrix

mtx = Matrix()
mtx.load_from_file("matrix_v2.json")

query_string = "SELECT * FROM people WHERE birthdate.dow"

query = {
    "command": "select",
    "selectors": [
        {
            "attribute": "birthdate_dow",
            "operator": "equals",
            "value": "mon"
        }
    ]
}

r = mtx.query(query_string)
for i in r:
    print(i)

i = mtx.items[0]


# me = mtx.search("max a")[0]
# y = me.school_years[0]
# sem = y.semesters[1]
# sch = sem.schedule
# rot = sch.rotations[1]
# for cl in rot.classes:
#
#     print(cl.name if not cl.is_free else "free")
