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
    description: Optional[str] = None
    state: Optional[str] = None

@app.get('/')
async def getAll():
    """ Get all resources

    Returns
    -------
    def
        returns response from script

    """
    return [json.loads(cluster.export()) for cluster in clusters.get_all]

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
        raise HTTPException(status_code=404, detail="Cluster not found")

    return json.loads(cluster.export())


@app.post('/')
async def create(body: Body):
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
    cluster = clusters.create(body.dict())
    execution_code = cluster.startup()
    return json.loads(cluster.export())

@app.put('/{id}')
async def update(id, body: Body):
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
        raise HTTPException(status_code=404, detail="Cluster not found")

    cluster.update(body.dict())

    return json.loads(cluster.export())

@app.delete('/{id}')
async def delete(id):
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
        raise HTTPException(status_code=404, detail="Cluster not found")

    execution_code = cluster.shutdown()
    return {"message" : "deleting cluster"}
