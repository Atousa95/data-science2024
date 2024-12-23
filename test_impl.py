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
        self.rel_path = "relational.db"
        self.csv_path = "meta.csv"
        self.upload = Upload()
        self.upload.setDbPath(self.rel_path)
        self.upload.uploadData(self.csv_path)
        self.query = Query()
        self.query.setDbPath(self.rel_path)

    def test_get_all_people(self):
        result = self.query.getAllPeople()
        self.assertIsInstance(result, list)
        self.assertTrue(all(isinstance(person, Person) for person in result))

    def test_get_all_cultural_heritage_objects(self):
        result = self.query.getAllCulturalHeritageObjects()
        self.assertIsInstance(result, list)
        self.assertTrue(all(isinstance(obj, CulturalHeritageObject) for obj in result))

    def test_get_cultural_heritage_object_by_type(self):
        result = self.query.getCulturalHeritageObjectByType("Nautical chart")
        self.assertIsInstance(result, list)
        self.assertTrue(all(isinstance(obj, CulturalHeritageObject) for obj in result))
        self.assertTrue(all(obj.getType() == "Nautical chart" for obj in result))

if __name__ == '__main__':
    unittest.main()
