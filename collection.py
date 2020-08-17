import json

class BaseCollection(object):
    """BaseModel for inheritance on any objects moving forwardx"""

    def __init__(self, meta_type, data):
        super(BaseCollection, self).__init__()
        self._ = {"index": {"id": {}}}
        self._items = []
        self.meta_type = meta_type;

        if data is not None:
            self.create_batch(data)

    @property
    def get_all(self):
        return self._items

    @property
    def get_count(self):
        return len(self._items)

    def create(self, data):
        obj = None

        if data is not None and isinstance(data, dict):
            obj = self.meta_type(data)
            self._items.append(obj)
            self._["index"]["id"][obj.id] = obj

        return obj

    def create_batch(self, data):
        set = list()

        if data is not None and isinstance(data, list):
            set = [self.create(d) for d in data]

        return set

    def is_meta_type(self, item):
        return item is not None and isinstance(item, self.meta_type)

    def export(self):
        return json.dumps({"items" : [item.export() for item in self.get_all]})

    def get_by_id(self, id):
        obj = self._["index"]["id"][id]

        if obj is not None:
            return obj

        return next((item for item in self._items if item.id == id), None)
