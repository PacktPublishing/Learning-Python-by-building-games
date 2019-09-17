import pymunk as p
from pymunk import Vec2d


class RoundBird():
    def __init__(self, distance, angle, x_pos, y_pos, space):
        weight = 5
        r = 12  # radius
        value_of_inertia = p.moment_for_circle(weight, 0, r, (0, 0))
        obj_body = p.Body(weight, value_of_inertia)
        obj_body.position = x_pos, y_pos
        power_value = distance * 53
        impulse = power_value * Vec2d(1, 0)
        angle = -angle
        obj_body.apply_impulse_at_local_point(impulse.rotated(angle))
        obj_shape = p.Circle(obj_body, r, (0, 0))
        obj_shape.elasticity = 0.95  # bouncing angry bird
        obj_shape.friction = 1  # for roughness
        obj_shape.collision_type = 0  # for checking collisions later
        space.add(obj_body, obj_shape)
        # class RoundBird attribute ----
        self.body = obj_body
        self.shape = obj_shape


class RoundPig():
    def __init__(self, x_pos, y_pos, space):
        # life will be decreased after collision of pig with bird
        self.life = 20
        weight = 5
        r = 14  # r adius
        value_of_inertia = p.moment_for_circle(weight, 0, r, (0, 0))
        obj_body = p.Body(
            weight, value_of_inertia)  # creates virtual space to render shape
        obj_body.position = x_pos, y_pos
        # add circle to obj body
        obj_shape = p.Circle(obj_body, r, (0, 0))
        obj_shape.elasticity = 0.95
        obj_shape.friction = 1
        obj_shape.collision_type = 1
        space.add(obj_body, obj_shape)
        self.body = obj_body
        self.shape = obj_shape
