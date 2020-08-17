from processor import AsyncProcessor
from enum import Enum

class State(str, Enum):
    """docstring for State."""
    Off = 'off'
    StartingUp = 'starting_up'
    On = 'on'
    ShuttingDown = 'shutting_down'

class Cluster(AsyncProcessor):
    """docstring for ."""

    def __init__(self, data):
        super(Cluster, self).__init__(data)

        if self.state is None:
            self.state = State.Off

    @property
    def id(self):
        return self.get('id', None)

    @id.setter
    def id(self, id):
        self.set('id', id, int)

    @property
    def create_script_command(self):
        return self.get('create_script_command', None)

    @create_script_command.setter
    def create_script_command(self, path):
        self.set('create_script_command', path, list)

    @property
    def shutdown_script_command(self):
        return self.get('shutdown_script_command', None)

    @shutdown_script_command.setter
    def shutdown_script_command(self, path):
        self.set('shutdown_script_command', path, list)

    @property
    def state(self):
        return self.get('state', None)

    @state.setter
    def state(self, state):
        self.set('state', state, State)

    def startup(self):
        self.state = State.StartingUp
        execution_code = self.execute(
            self.create_script_command,
            lambda x: print("STDOUT: %s" % x),
            lambda x: print("STDERR: %s" % x),
        )
        self.state = State.On
        return execution_code

    def shutdown(self):
        self.state = State.ShuttingDown
        execution_code = self.execute(
            self.shutdown_script_command,
            lambda x: print("STDOUT: %s" % x),
            lambda x: print("STDERR: %s" % x),
        )
        self.state = State.Off
        return execution_code
