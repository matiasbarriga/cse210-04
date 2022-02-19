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
        self._text = ""

    def is_rock(self):
        """
        "o" is the text representation of a rock
        """

        return self._text == "o"

    def is_gem(self):
        """
        "*" is the text representation of a gem
        """
        return self._text == "*"
    
    def set_text(self, text):

        self._text = text