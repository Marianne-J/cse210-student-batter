from game.action import Action

class DrawActorsAction:
    """A code template for drawing actors. The responsibility of this
    class of objects is draw the actors on the screen.
    
    Stereotype:
        Service Provider

    Attributes:
        _output_service (OutputService): An instance of OutputService.
    """

    def __init__(self, output_service):
        """The class constructor.
        
        Args:
            output_service (OutputService): An instance of OutputService.
        """
        self._output_service = output_service
    
    def execute(self, cast):
        """uses the output_service attribute to draw the actors on the screen.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """