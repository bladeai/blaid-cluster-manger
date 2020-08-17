from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Body(BaseModel):
    """ Model of data structure passed to the API call as body

    Attributes
    ----------
    description: Optional[str] : type
        Description of attribute `description: Optional[str]`.

    """
    name: str
    description: Optional[str] = None

@app.get('/')
async def getAll():
    """ Get all resources

    Returns
    -------
    def
        returns response from script

    """
    return process_response(subprocess.run(['sh', './getAll.sh'],
    stdout=subprocess.PIPE))

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
    process = subprocess.run(['sh', './getByID.sh', str(id)],
                         stdout=subprocess.PIPE,
                         universal_newlines=True)
    return {'message' : process.stdout}


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
    process = subprocess.run(['sh', './create.sh', str(body)],
                         stdout=subprocess.PIPE,
                         universal_newlines=True)
    return process_response(process)

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
    process = subprocess.run(['sh', './update.sh', str(id), str(body)],
                         stdout=subprocess.PIPE,
                         universal_newlines=True)
    return process_response(process)

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
    process = subprocess.run(['sh', './delete.sh'],
                         stdout=subprocess.PIPE,
                         universal_newlines=True)
    return {'message' : process.stdout}


def process_response(process):
    """Method to process all script reponses

    Parameters
    ----------
    process : type
        Description of parameter `process`.

    Returns
    -------
    type
        returns error or message depending on returned stderr or stdout

    """
    if process.stderr is not None:
        return {'error' : process.stderr}
    return {'message' : process.stdout}
