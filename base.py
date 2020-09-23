import json

class BaseModel(object):
    """BaseModel for inheritance on any objects moving forwardx"""

    def __init__(self, data = {}):
        super(BaseModel, self).__init__()
        self._ = {}
        self.update(data)

    def get(self, prop, _default):
        """ Getter method to retrieve property

        Parameters
        ----------
        prop : String
            name of property to search for.
        _default : Any
            default return if property doees not exists.

        Returns
        -------
        type
            returned object pf property requested.

        """
        return self._.get(prop, _default)

    def set(self, prop, val, constructor):
        """ Setter method to insert property

        Parameters
        ----------
        prop : String
            Property name.
        val : Any
            property value to insert.
        constructor : Any
            constructor type to validate.

        """
        if val and isinstance(val, constructor):
            self._[prop] = val

    def update(self, data={}):
        for key in data:
            self._[key] = data[key]

    def export(self):
        self._['id'] = str(self._['_id'])
        del self._['_id']
        return self._

    @property
    def id(self):
        return self.get('_id', None)

    @property
    def extensors(self):
        return self.get('extensors', {})

    @extensors.setter
    def extensors(self, extensors):
        self.set('extensors', extensors, dict)

    @property
    def record_history(self):
        return self.get('record_history', None)

    @record_history.setter
    def record_history(self, record):
        self.set('record_history', record, dict)

    @property
    def created_at(self):
        record = self.record_history
        return record.get('created_at', None)

    @property
    def created_by(self):
        record = self.record_history
        return record.get('created_by', None)

    @property
    def created_by_type(self):
        record = self.record_history
        return record.get('created_by_type', None)

    @property
    def updated_at(self):
        record = self.record_history
        return record.get('updated_at', None)

    @updated_at.setter
    def updated_at(self, time):
        record = self.record_history
        record['updated_at'] = time
        self.record_history = record

    @property
    def updated_by(self):
        record = self.record_history
        return record.get('updated_by', None)

    @property
    def updated_by_type(self):
        record = self.record_history
        return record.get('updated_by_type', None)
