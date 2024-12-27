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


# Supposing that all the classes developed for the project
# are contained in the file 'impl.py', then:

# 1) Importing all the classes for creating the relational database
from impl import Upload

# 3) Importing the class for querying the database
from impl import Query

# Once all the classes are imported, first create the relational
# database using the related source data
rel_path = "relational.db"
ul = Upload()
ul.setDbPath(rel_path)
ul.uploadData("meta.csv")

# In the next passage, create the query object for the
# database, using the related class
qy = Query()
qy.setDbPath(rel_path)

# Finally, you run the methods querying the database
result_q1 = qy.getAllPeople()
result_q2 = qy.getCulturalHeritageObjectByType("Nautical chart")
# etc...