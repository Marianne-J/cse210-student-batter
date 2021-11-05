from game import constants
from game.action import Action
from game.point import Point

class MoveActorsAction(Action):
    """A code template for moving actors. The responsibility of this class of
    objects is move any actor that has a velocity more than zero.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        for group in cast.values():
            for actor in group:
                if not actor.get_velocity().is_zero():
                    self._move_actor(actor)

    def _move_actor(self, actor):
        """Moves the given actor to its next position according to its 
        velocity. Bounces the ball off the edges of the screen and changes
        its velocity.
        
        Args:
            actor (Actor): The actor to move.
        """
        position = actor.get_position()
        velocity = actor.get_velocity()
        x1 = position.get_x()
        y1 = position.get_y()
        if x1 <= 0:
            x1 = 1
            x2 = - velocity.get_x()
        elif x1 >= constants.MAX_X:
            x1 = constants.MAX_X - 1
            x2 = - velocity.get_x()
        elif y1 <= 0:
            y1 = 1
            y2 = - velocity.get_y()
        elif y1 >= constants.MAX_Y:
            y1 = constants.MAX_Y - 1
            y2 = - velocity.get_y()
        else:
            x2 = velocity.get_x()
            y2 = velocity.get_y()
        x = 1 + (x1 + x2 - 1) % (constants.MAX_X - 1)
        y = 1 + (y1 + y2 - 1) % (constants.MAX_Y - 1)
        position = Point(x, y)
        actor.set_position(position)