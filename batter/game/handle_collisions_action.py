import sys
from game import constants
from game.action import Action

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors. This action is checking for a collision and 
        reversing the velocity if a collision is detected. Also ends the game if a floor collision occurs.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast["ball"][0] # there's only one
        paddle = cast["paddle"][0] # there's only one
        bricks = cast["brick"]

        ball_pos = ball.get_position()
        ball_vel = ball.get_velocity()
        ball_next_x = ball_pos.get_x() + ball_vel.get_x()
        ball_next_y = ball_pos.get_y() + ball_vel.get_y()

        paddle_pos = paddle.get_position()

        # wall collision
        if (ball_next_x <= 0 or ball_next_x >= constants.MAX_X):
            ball.set_velocity(ball_pos.reverse_x())
        # ceiling collision
        elif (ball_next_y <= 0):
            ball.set_velocity(ball_pos.reverse_y())
        # floor collision, ends the game if true
        elif (ball_next_y >= constants.MAX_Y):
            sys.exit()
        # paddle collision, checks vertically
        elif ( ball_next_y == paddle_pos.get_y() ) and ( ball_pos.get_x() == paddle_pos.get_x() ):
            ball.set_velocity(ball_pos.reverse_y())
        # brick collision
        else:
            for x in range(len(bricks)):
                brick_pos = bricks[x].get_position()
                collision = False

                # horizontal collision check on next move
                if ( ball_next_x == brick_pos.get_x() ) and ( ball_pos.get_y() == brick_pos.get_y() ):
                    collision = True
                    ball.set_velocity(ball_pos.reverse_x())
                # vertical collision check on next move
                elif ( ball_next_y == brick_pos.get_y() ) and ( ball_pos.get_x() == brick_pos.get_x() ):
                    collision = True
                    ball.set_velocity(ball_pos.reverse_y())
                # diagonal collision check on next move
                elif ( ball_next_x == brick_pos.get_x() ) and ( ball_next_y == brick_pos.get_y() ):
                    collision = True
                    ball.set_velocity(ball_pos.reverse())

                if collision:
                    bricks.pop(x)