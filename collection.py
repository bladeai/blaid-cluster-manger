import json
from uuid import uuid4
from pymongo import MongoClient
from bson.objectid import ObjectId
from config import db_url, db_name
import time

class BaseCollection(object):
    """BaseModel for inheritance on any objects moving forwardx"""

    def __init__(self, meta_type, collection_name):
        super(BaseCollection, self).__init__()

        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]
        self.meta_type = meta_type;

    def get_all(self):
        return self.get_by_query({})

    def get_count(self):
        return len(self.get_all)

    def get_by_id(self, id):
        item = self.collection.find_one({'_id': ObjectId(id)})
        if item is not None:
            return self.meta_type(item)
        return None

    def get_by_query(self, query):
        return [self.meta_type(item) for item in self.collection.find(query)]

    def create(self, data):
        data['record_history'] = {}
        data['record_history']['created_at'] = int(time.time())
        item = self.collection.insert_one(data)
        return self.get_by_id(item.inserted_id)

    def create_batch(self, data):
        set = list()

        if data is not None and isinstance(data, list):
            items = self.collection.insert_many(data)
            set = [self.meta_type(self.get_by_id(id)) for id in items.inserted_ids]

        return set

    def update(self, item):
        if item is not None and isinstance(item, self.meta_type):
            item.updated_at = int(time.time())
            data = item.export()
            del data['id']
            self.collection.update_one({'_id': item.id}, {'$set': data})
            return item
        return None

    def delete(self, item):
        if item is not None and isinstance(item, self.meta_type):
            return self.collection.delete_one({'_id': item.id})
        return None
