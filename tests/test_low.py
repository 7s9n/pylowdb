import unittest
import json
import os

from pylowdb import MissingAdapterError
from pylowdb import Low, JsonFile


def create_json_file(data):
    filename = 'tempfile.temp'

    with open(filename, 'w') as tmp:
        tmp.write(json.dumps(data))

    return filename


class LowTestCase(unittest.TestCase):
    def test_no_adapter(self):
        self.assertRaises(MissingAdapterError, Low)

    def test_low(self):
        data = {'a': 1}
        file = create_json_file(data)

        # Init
        adapter = JsonFile(file)
        db = Low(adapter)

        db.read()

        # Data should equal file content
        self.assertDictEqual(db.data, data)

        # Write new data
        new_data = {'b': 2}
        db.data = new_data
        db.write()

        # File content should equal new data
        with open(file, 'r') as f:
            data = f.read()

        self.assertEqual(json.loads(data), new_data)

        os.remove(file)


if __name__ == '__main__':
    unittest.main()
