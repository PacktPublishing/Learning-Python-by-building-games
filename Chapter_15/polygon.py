import pymunk as pym
from pymunk import Vec2d
import pygame as pg
import math


class Polygon():
    def __init__(self, position, length, height, space, mass=5.0):
        value_moment = 1000
        body_obj = pym.Body(mass, value_moment)
        body_obj.position = Vec2d(position)
        shape_obj = pym.Poly.create_box(body_obj, (length, height))
        shape_obj.color = (0, 0, 255)
        shape_obj.friction = 0.5
        shape_obj.collision_type = 2  # adding to check collision later
        space.add(body_obj, shape_obj)
        self.body = body_obj
        self.shape = shape_obj
        wood_photo = pg.image.load("./res/photos/wood.png").convert_alpha()
        wood2_photo = pg.image.load("./res/photos/wood2.png").convert_alpha()
        rect_wood = pg.Rect(251, 357, 86, 22)
        self.beam_image = wood_photo.subsurface(rect_wood).copy()
        rect_wood2 = pg.Rect(16, 252, 22, 84)
        self.column_image = wood2_photo.subsurface(rect_wood2).copy()

    def convert_to_pygame(self, pos):
        """Convert pymunk to pygame coordinates"""
        return int(pos.x), int(-pos.y + 610)

    def draw_poly(self, element, screen):
        """Draw beams and columns"""
        polygon = self.shape

        if element == 'beams':
            pos = polygon.body.position
            pos = Vec2d(self.convert_to_pygame(pos))
            angle_degrees = math.degrees(polygon.body.angle)
            rotated_beam = pg.transform.rotate(self.beam_image, angle_degrees)
            offset = Vec2d(rotated_beam.get_size()) / 2.
            pos = pos - offset
            final_pos = pos
            screen.blit(rotated_beam, (final_pos.x, final_pos.y))
        if element == 'columns':
            pos = polygon.body.position
            pos = Vec2d(self.convert_to_pygame(pos))
            angle_degrees = math.degrees(polygon.body.angle) + 180
            rotated_column = pg.transform.rotate(self.column_image,
                                                 angle_degrees)
            offset = Vec2d(rotated_column.get_size()) / 2.
            pos = pos - offset
            final_pos = pos
            screen.blit(rotated_column, (final_pos.x, final_pos.y))
