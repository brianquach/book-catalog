"""
Copyright 2016 Brian Quach
Licensed under MIT (https://github.com/brianquach/udacity-nano-fullstack-catalog/blob/master/LICENSE)  # noqa
"""
import json
from catalog import db
from catalog.models import Catagory
from catalog.models import CatagoryItem


# Create database schema

db.create_all()

# Create and add default catagories (book genres) with their respective items

catagories = json.loads(open('test_data.json', 'r').read())['Catagories']
for c in catagories:
    catagory = Catagory(name=c["Name"])
    db.session.add(catagory)
    db.session.flush()

    if 'Items' in c:
        for i in c["Items"]:
            item = CatagoryItem(
                name=i["Name"],
                author=i["Author"],
                description=i["Description"],
                picture=i["Picture"],
                catagory_id=catagory.id
            )
            db.session.add(item)
db.session.commit()
