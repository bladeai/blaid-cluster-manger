from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel
import json
from clusters import ClusterCollection

app = FastAPI()

clusters = ClusterCollection()

class Body(BaseModel):
    """ Model of data structure passed to the API call as body

    Attributes
    ----------
    description: Optional[str] : type
        Description of attribute `description: Optional[str]`.

    """
    name: str

@app.get('/')
async def getAll():
    """ Get all resources

    Returns
    -------
    def
        returns response from script

    """
    return [cluster.export() for cluster in clusters.get_all()]

@app.get('/{id}')
async def get(id):
    """ Get resource by ID

    Parameters
    ----------
    id : type
        identifier of resource being retrieved

    Returns
    -------
    def
        returns response from script

    """
    cluster = clusters.get_by_id(id)

    if cluster is None:
        raise HTTPException(status_code=404, detail="Cluster not found for ID: {0}".format(id))

    return cluster.export()


@app.post('/')
def create(body: Body):
    """ Create resource

    Parameters
    ----------
    body : Body
        Body of information to create

    Returns
    -------
    def
        returns response from script

    """
    cluster = clusters.get_by_query(body.dict())

    if len(cluster) > 0:
        raise HTTPException(status_code=400, detail="Cluster already exists")

    cluster = clusters.create(body.dict())
    # execution_code = cluster.startup()
    return cluster.export()

@app.put('/{id}')
def update(id, body: Body):
    """ Update resource by ID

    Parameters
    ----------
    id : type
        identifier of resource
    body : Body
        Body of information to update

    Returns
    -------
    def
        returns response from script

    """

    cluster = clusters.get_by_id(id)

    if cluster is None:
        raise HTTPException(status_code=404, detail="Cluster not found for ID: {0}".format(id))

    cluster.update(body.dict())
    cluster = clusters.update(cluster)

    return cluster.export()

@app.delete('/{id}')
def delete(id):
    """Delete resource by ID

    Parameters
    ----------
    id : type
        identifier of resource

    Returns
    -------
    def
        returns response from script

    """
    cluster = clusters.get_by_id(id)

    if cluster is None:
        raise HTTPException(status_code=404, detail="Cluster not found for ID: {0}".format(id))

    results = clusters.delete(cluster)

    if results.acknowledged:
        return {"message" : "cluster deleted"}
    raise HTTPException(status_code=400, detail=results.raw_result)
