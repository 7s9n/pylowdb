# Pylowdb

[![Downloads](https://pepy.tech/badge/pylowdb)](https://pepy.tech/project/pylowdb)
[![Downloads](https://pepy.tech/badge/pylowdb/month)](https://pepy.tech/project/pylowdb)

> Simple to use local JSON database 🦉

```python
# This is pure python, not specific to pylowdb ;)
db.data['posts'] = ({ 'id': 1, 'title': 'pylowdb is awesome' })

# Save to file
db.write()
```

```python
# db.json
{
  "posts": [
    { "id": 1, "title": "pylowdb is awesome" }
  ]
}
```

## Support me

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/HusseinSarea)

## Features

- __Lightweight__
- __Minimalist__ and easy to learn API
- Query and modify data using __plain Python__
- Atomic write
- Hackable:
  - Change storage, file format (JSON, YAML, ...) or add encryption via [adapters](#adapters)

## Install

```python
pip install pylowdb
```

## Usage

```python
import os
from os import path
from pylowdb import (
    Low,
    JSONFile,
)

# Use JSON file for storage
file = path.join(os.getcwd(), 'db.json')
adapter = JSONFile(file)
db = Low(adapter)

# Read data from JSON file, this will set db.data content
db.read()

# If file.json doesn't exist, db.data will be None
# Set default data
# db.data = db.data or { 'posts': [] }
db.data = db.data or { 'posts': [] }

# Create and query items using plain Python

db.data['posts'].append('hello world')
db.data['posts'][0]

# You can also use this syntax if you prefer
posts = db.data['posts']
posts.append('hello world'

# Write db.data content to db.json
db.write()
```

```JSON
// db.json
{
  "posts": [ "hello world" ]
}
```

### More examples

For more example, see [`examples/`](/examples) directory.

## API

### Classes

Pylowdb has two classes (for synchronous adapters).

#### `Low(adapter)`

```python
from pylowdb import (
    Low,
    JSONFile,
)
db = Low(JSONFile('file.json'))
db.read()
db.write()
```

### Methods

#### `db.read()`

Calls `adapter.read()` and sets `db.data`.

**Note:** `JSONFile` adapter will set `db.data` to `None` if file doesn't exist.

```python
db.data  # is None
db.read()
db.data # is not None
```

#### `db.write()`

Calls `adapter.write(db.data)`.

```python
db.data = { 'posts': [] }
db.write() # file.json will be { posts: [] }
db.data = {}
db.write() # file.json will be {}
```

### Properties

#### `db.data`

Holds your db content. If you're using the adapters coming with pylowdb, it can be any type supported by [`json.dumbs`](https://docs.python.org/3/library/json.html).

For example:

```python
db.data = 'string'
db.data = [1, 2, 3]
db.data = { 'key': 'value' }
```

## Adapters

### Pylowdb adapters

#### `JSONFile`

Adapter for reading and writing JSON files.

```python
Low(JSONFile(filename))
```

#### `Memory`

In-memory adapter. Useful for speeding up unit tests.

```python
Low(Memory())
```

#### `YAMLFile`

Adapter for reading and writing YAML files.

```python
Low(YAMLFile(filename))
```

#### `TextFile`

Adapters for reading and writing text. Useful for creating custom adapters.

### Third-party adapters

If you've published an adapter for pylowdb, feel free to create a PR to add it here.

### Writing your own adapter

You may want to create an adapter to write `db.data` to YAML, XML, encrypt data, a remote storage, ...

An adapter is a simple class that just needs to expose two methods:

```python
class CustomAdapter:
    read(self):
        # should return deserialized data
        pass
    write(self, data):
        # should return nothing
        pass
```

For example, let's say you have some async storage and want to create an adapter for it:

```python
api = YourAPI()

class CustomAdapter:
    # Optional: your adapter can take arguments

    def __init__(self, *args, **kwargs):
        pass

    def read(self):
        data = api.read()
    return data

    def write(self, data):
        api.write(data)

adapter = CustomAdapter()
db = Low(adapter)
```

See [`pylowdb/adapters`](pylowdb/adapters.py) for more examples.

#### Custom serialization

To create an adapter for another format than JSON, you can use
`TextFile`.

For example:

```python
from pylowdb import (
    Adapter,
    Low,
    TextFile,
)
import yaml

class YAMLFile(Adapter):
    def __init__(self, filename: str):
        self.adapter = TextFile(filename)

    def read(self):
        data = self.adapter.read()
        if data is None:  
            return null
        else:
            return YAML.deserialize(data)

    def write(self, obj):
        return self.adapter.write(YAML.serialize(obj))

adapter = YAMLFile('file.yaml')
db = Low(adapter)
```

## Limits

If you have large Python objects (`~10-100MB`) you may hit some performance issues. This is because whenever you call `db.write`, the whole `db.data` is serialized and written to storage.

Depending on your use case, this can be fine or not. It can be mitigated by doing batch operations and calling `db.write` only when you need it.

If you plan to scale, it's highly recommended to use databases like PostgreSQL, MySql, Oracle ...
