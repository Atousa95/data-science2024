# -*- coding: utf-8 -*-
# Copyright (c) 2023, Silvio Peroni <essepuntato@gmail.com>
#
# Permission to use, copy, modify, and/or distribute this software for any purpose
# with or without fee is hereby granted, provided that the above copyright notice
# and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT,
# OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE,
# DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS
# ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS
# SOFTWARE.

import unittest
from impl import Upload, Query, Person, CulturalHeritageObject

class TestImpl(unittest.TestCase):
    def setUp(self):
        
        print("Start setUp Function: ")
        self.rel_path = "relational.db"
        self.csv_path = "meta.csv"
        self.upload = Upload()
        self.upload.setDbPath(self.rel_path)
        self.upload.uploadData(self.csv_path)
        self.query = Query()
        self.query.setDbPath(self.rel_path)

    def test_get_all_people(self):
        for _ in range(3):
            print()
        result = self.query.getAllPeople()
        print("-----::Get All People::-----")
        for row_number, obj in enumerate(result, start=1):
            print(f"\tRow {row_number} : {obj.name}")
        for _ in range(3):
            print()
        self.assertIsInstance(result, list)
        self.assertTrue(all(isinstance(person, Person) for person in result))

    def test_get_all_cultural_heritage_objects(self):
        for _ in range(3):
            print()
        result = self.query.getAllCulturalHeritageObjects()
        print("-----::Get All Cultural Heritage Objects::-----")
        for row_number, obj in enumerate(result, start=1):
            print(f"\tRow {row_number} : {obj.type}")
        for _ in range(3):
            print()
        self.assertIsInstance(result, list)
        self.assertTrue(all(isinstance(obj, CulturalHeritageObject) for obj in result))

    def test_get_cultural_heritage_object_by_type(self):
        for _ in range(3):
            print()
            listTypes=["Nautical chart", "Printed volume", "Herbarium", "Printed material", "Specimen"]
        for type in listTypes:
            print("-----::Get All Cultural Heritage Objects::-----")
            print(f"\tType: {type}")
            result = self.query.getCulturalHeritageObjectByType(type)
            for row_number, obj in enumerate(result, start=1):
                print(f"\t\tRow {row_number} : {obj.title}")
        self.assertIsInstance(result, list)
        self.assertTrue(all(isinstance(obj, CulturalHeritageObject) for obj in result))

if __name__ == '__main__':
    print("------------------Starting UnitTest-----------------")
    for _ in range(3):
            print()
    unittest.main()
