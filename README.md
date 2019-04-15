# PyMTX
##### By Max Koon

*A python interface for the Matrix Database*

### Usage

```python
# import the package
from matrix import Matrix
# create the instance 
mtx = Matrix()
# load a file
mtx.load_from_file("matrix.json")
# or load from a url
mtx.load_from_url("https://example.com/people.json", True)
#                                      refreshes cache ^
```

### Creating a Database (TODO)
If you do not have a database you can do
```python
# creates a blank database
mtx.create_db("new_matrix.json")
```

### Querying from a Database

commands:

- select
- remove
- update
- insert

methods

main: query(string)

query_array = parse_query_string(string)

items = select_items_from_query_array(query_array)

#### select_items_from_query_array(query_array)

selectors = query_array['selectors']

selectors inc. 

- groups
- 

