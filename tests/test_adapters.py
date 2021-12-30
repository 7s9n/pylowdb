import unittest
import os
from pylowdb import (
    JsonFile,
    Memory,
    TextFile,
    YAMLFile,
)


class JsonFileTestCase(unittest.TestCase):
    def test_json_file(self):
        data = {'a': 1}
        filename = 'tempfile.temp'
        file = JsonFile(filename)

        self.assertIsNone(file.read())

        # Write
        self.assertIsNone(file.write(data))

        # Read
        self.assertEqual(data, file.read())

        os.remove(filename)


class TextFileTestCase(unittest.TestCase):
    def test_text_file(self):
        data = 'Hello world'
        filename = 'tempfile.temp'
        file = TextFile(filename)

        self.assertIsNone(file.read())

        # Write
        self.assertIsNone(file.write(data))

        # Read
        self.assertEqual(data, file.read())

        os.remove(filename)


class YAMLFileTestCase(unittest.TestCase):
    def test_yaml_file(self):
        data = [1, 2, 3, {'Title': 'Hussein Sarea'}]
        filename = 'tempfile.temp'
        file = YAMLFile(filename)

        self.assertIsNone(file.read())

        # Write
        self.assertIsNone(file.write(data))

        # Read
        self.assertEqual(data, file.read())

        os.remove(filename)


class MemoryTestCase(unittest.TestCase):
    def test_memory(self):
        data = {'a': 1}
        memory = Memory()

        # Null by default
        self.assertIsNone(memory.read())

        # Write
        self.assertIsNone(memory.write(data))

        # Read
        self.assertEqual(data, memory.read())


if __name__ == '__main__':
    unittest.main()
