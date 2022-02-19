from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!

class Artifact(Actor):

    def __init__(self):
        """
        invokes an instance of the Actor Class to inherit its attributes and methods.

        Attributes:
            self._message = the message that the artifact holds
        """
        super().__init__()
        self._message = ""

    def get_message(self):
        """
        return the message of the artifact
        """
        return self._message

    def set_message(self, message):
        """
        Set the message that the artifact will hold
        """
        self._message = message