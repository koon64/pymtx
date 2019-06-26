from matrix import Matrix

mtx = Matrix()

mtx.load_from_url("https://www.zoos-tech.com/api/mtx_query?query=select%20*%20from%20students&key=fedcba")

me = mtx.name_match("max a")

print(me)