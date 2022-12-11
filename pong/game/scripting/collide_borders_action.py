from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBordersAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service

    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BALL_GROUP)
        body = ball.get_body()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()
        hit_sound = Sound(HIT_SOUND)
        gameover_sound = Sound(GAMEOVER_SOUND)
        racket1 = cast.get_first_actor(RACKET_GROUP[0])
        racket2 = cast.get_first_actor(RACKET_GROUP[1])
        stats1 = cast.get_first_actor(STATS_GROUP1)
        stats2 = cast.get_first_actor(STATS_GROUP2)
        score1 = stats1.get_score()
        score2 =stats2.get_score()

        if x <= FIELD_LEFT:
            points2 = racket2.get_points()
            stats2.add_points(points2)

            if score1 == 2 or score2 == 2:
                callback.on_next(GAME_OVER)
                self._audio_service.play_sound(gameover_sound)
            else:
                callback.on_next(TRY_AGAIN)

        elif x >= (FIELD_RIGHT - BALL_WIDTH):
            points1 = racket1.get_points()
            stats1.add_points(points1)

            if score2 ==2 or score1 ==2:
                callback.on_next(GAME_OVER)
                self._audio_service.play_sound(gameover_sound)
            else:
                callback.on_next(TRY_AGAIN)

        if y <= FIELD_TOP:
            ball.bounce_y()
            self._audio_service.play_sound(hit_sound)

        elif y >= (FIELD_BOTTOM - BALL_HEIGHT):
            ball.bounce_y()
            self._audio_service.play_sound(hit_sound)
        
        