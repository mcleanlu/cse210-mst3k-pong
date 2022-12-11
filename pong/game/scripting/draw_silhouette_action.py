from constants import *
from game.scripting.action import Action


class DrawSilhouetteAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service

    def execute(self, cast, script, callback):
        silhouette = cast.get_first_actor(SILHOUETTE_GROUP)
        body = silhouette.get_body()

        if silhouette.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, RED)

        image = silhouette.get_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)