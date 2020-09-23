from collection import BaseCollection
from cluster import Cluster

class ClusterCollection(BaseCollection):
    """docstring for ClusterCollection."""

    def __init__(self):
        super(ClusterCollection, self).__init__(Cluster, 'clusters')
