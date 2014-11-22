#
# This file is where you make the display for your game
# Make changes and add functions as you need.
#
import random
import os
import math
import pygame
from config import *
from common.event import *
from client.base_display import BaseDisplay

class Display(BaseDisplay):
    """
    This class controls all of the drawing of the screen
    for your game.  The process of drawing a screen is
    to first draw the background, and then draw everything
    that goes on top of it.  If two items are drawn in the
    same place, then the last item drawn will be the one
    that is visible.

    The screen is a 2 dimensional grid of pixels, with the
    origin (0,0) located at the top-left of the screen, and
    x values increase to the right and y values increase as
    you go down.  The y values are opposite of what you learned
    in your math classes.

    Documentation on drawing in pygame is available here:
    http://www.pygame.org/docs/ref/draw.html

    The methods in this class are:
    __init__ creates data members (variables) that are used
        in the rest of the methods of this class.  This is
        useful for defining colors and sizes, loading image
        or sound files, creating fonts, etc.  Basically,
        any one time setup.

    paint_game controls the drawing of the screen while the
        game is in session.  This is responsible for making
        sure that any information, whether graphics, text, or
        images are drawn to the screen.

    paint_waiting_for_game controls the drawing of the screen
        after you have requested to join a game, but before
        the game actually begins.
    
    paint_game_over controls the drawing of the screen after
        the game has been won, but before the game goes away.
        This is a short (3-5 second) period.

    process_event controls handling events that occur in the
        game, that aren't represented by objects in the game
        engine.  This includes things like collisions,
        objects dying, etc.  This would be a great place to
        play an audio file when missiles hit objects.

    paint_pregame controls the drawing of the screen before
        you have requested to join a game.  This would usually
        allow the user to know the options available for joining
        games.

    Method parameters and data members of interest in these methods:
    self.width is the width of the screen in pixels.
    self.height is the height of the screen in pixels.
    self.* many data members are created in __init__ to set up
        values for drawing, such as colors, text size, etc.
    surface is the screen surface to draw to.
    control is the control object that is used to
        control the game using user input.  It may
        have data in it that influences the display.
    engine contains all of the game information about the current
        game.  This includes all of the information about all of
        the objects in the game.  This is where you find all
        of the information to display.
    event is used in process_event to communicate what
        interesting thing occurred.
    
    Note on text display:  There are 3 methods to assist
    in the display of text.  They are inherited from the
    BaseDisplay class.  See client/base_display.py.
    
    """
    def randomizer(self):
        return random.choice(range(4)) + 1

    def __init__(self, width, height):
        """
        Configure display-wide settings and one-time
        setup work here.
        """
        BaseDisplay.__init__(self, width, height)

        # There are other fonts available, but they are not
        # the same on every computer.  You can read more about
        # fonts at http://www.pygame.org/docs/ref/font.html
        self.title_font = pygame.font.SysFont("Courier new" , 22)
        self.font_size = 14
        self.font = pygame.font.SysFont("Courier New",self.font_size)

        # Colors are specified as a triple of integers from 0 to 255.
        # The values are how much red, green, and blue to use in the color.
        # Check out http://www.colorpicker.com/ if you want to try out
        # colors and find their RGB values.
        self.player_color     = (0, 255, 0)
        self.opponent_color   = (255, 0, 0)
        self.missile_color    = (0, 255, 255)
        self.npc_color        = (255, 255, 0)
        self.wall_color       = (255, 255, 255)
        self.text_color       = (255, 255, 255)
        self.background_color = (0, 0, 0)
        self.image_count      = 0
        self.sword_count = 0
        self.player_image_left1 = pygame.image.load(os.path.join("display", "Player", "NewPlayer_walkleft_1.png"))
        self.player_image_leftidle = pygame.image.load(os.path.join("display", "Player", "NewPlayer_idleleft.png"))
        self.player_image_left2 = pygame.image.load(os.path.join("display", "Player", "NewPlayer_walkleft_2.png"))
        self.player_image_right1 = pygame.image.load(os.path.join("display", "Player", "NewPlayer_walkright_1.png"))
        self.player_image_rightidle = pygame.image.load(os.path.join("display", "Player", "NewPlayer_idleright.png"))
        self.player_image_right2 = pygame.image.load(os.path.join("display", "Player", "NewPlayer_walkright_2.png"))
        self.player_image_up1 = pygame.image.load(os.path.join("display", "Player", "NewPlayer_walkup_1.png"))
        self.player_image_upidle = pygame.image.load(os.path.join("display", "Player", "NewPlayer_idleup.png"))
        self.player_image_up2 = pygame.image.load(os.path.join("display", "Player", "NewPlayer_walkup_2.png"))
        self.player_image_down1 = pygame.image.load(os.path.join("display", "Player", "NewPlayer_walkdown_1.png"))
        self.player_image_downidle = pygame.image.load(os.path.join("display", "Player", "NewPlayer_idledown.png"))
        self.player_image_down2 = pygame.image.load(os.path.join("display", "Player", "NewPlayer_walkdown_2.png"))

        self.opponent_image_left1 = pygame.image.load(os.path.join("display", "Enemy", "Enemy_walkleft_1.png"))
        self.opponent_image_leftidle = pygame.image.load(os.path.join("display", "Enemy", "Enemy_idleleft.png"))
        self.opponent_image_left2 = pygame.image.load(os.path.join("display", "Enemy", "Enemy_walkleft_2.png"))
        self.opponent_image_right1 = pygame.image.load(os.path.join("display", "Enemy", "Enemy_walkright_1.png"))
        self.opponent_image_rightidle = pygame.image.load(os.path.join("display", "Enemy", "Enemy_idleright.png"))
        self.opponent_image_right2 = pygame.image.load(os.path.join("display", "Enemy", "Enemy_walkright_2.png"))
        self.opponent_image_up1 = pygame.image.load(os.path.join("display", "Enemy", "Enemy_walkup_1.png"))
        self.opponent_image_upidle = pygame.image.load(os.path.join("display", "Enemy", "Enemy_idleup.png"))
        self.opponent_image_up2 = pygame.image.load(os.path.join("display", "Enemy", "Enemy_walkup_2.png"))
        self.opponent_image_down1 = pygame.image.load(os.path.join("display", "Enemy", "Enemy_walkdown_1.png"))
        self.opponent_image_downidle = pygame.image.load(os.path.join("display", "Enemy", "Enemy_idledown.png"))
        self.opponent_image_down2 = pygame.image.load(os.path.join("display", "Enemy", "Enemy_walkdown_2.png"))

        self.health_images = [
            pygame.image.load(os.path.join("display", "Health Bar", "HP10.png")),
            pygame.image.load(os.path.join("display", "Health Bar", "HP9.png")),
            pygame.image.load(os.path.join("display", "Health Bar", "HP8.png")),
            pygame.image.load(os.path.join("display", "Health Bar", "HP7.png")),
            pygame.image.load(os.path.join("display", "Health Bar", "HP6.png")),
            pygame.image.load(os.path.join("display", "Health Bar", "HP5.png")),
            pygame.image.load(os.path.join("display", "Health Bar", "HP4.png")),
            pygame.image.load(os.path.join("display", "Health Bar", "HP3.png")),
            pygame.image.load(os.path.join("display", "Health Bar", "HP2.png")),
            pygame.image.load(os.path.join("display", "Health Bar", "HP1.png")),
            pygame.image.load(os.path.join("display", "Health Bar", "HP0.png")),
        ]

        self.arrow_images = [
            None,
            pygame.image.load(os.path.join("display", "Arrow Count", "1Arrow.png")),
            pygame.image.load(os.path.join("display", "Arrow Count", "2Arrow.png")),
            pygame.image.load(os.path.join("display", "Arrow Count", "3Arrow.png")),
            pygame.image.load(os.path.join("display", "Arrow Count", "4Arrow.png")),
            pygame.image.load(os.path.join("display", "Arrow Count", "5Arrow.png")),
            pygame.image.load(os.path.join("display", "Arrow Count", "6Arrow.png")),
            pygame.image.load(os.path.join("display", "Arrow Count", "7Arrow.png")),
            pygame.image.load(os.path.join("display", "Arrow Count", "8Arrow.png")),
            pygame.image.load(os.path.join("display", "Arrow Count", "9Arrow.png")),
            pygame.image.load(os.path.join("display", "Arrow Count", "10Arrow.png")),
        ]

        self.mana_image = [
        pygame.image.load(os.path.join("display", "Movement Mana", "MovementMana10.png")),
        pygame.image.load(os.path.join("display", "Movement Mana", "MovementMana9.png")),
        pygame.image.load(os.path.join("display", "Movement Mana", "MovementMana8.png")),
        pygame.image.load(os.path.join("display", "Movement Mana", "MovementMana7.png")),
        pygame.image.load(os.path.join("display", "Movement Mana", "MovementMana6.png")),
        pygame.image.load(os.path.join("display", "Movement Mana", "MovementMana5.png")),
        pygame.image.load(os.path.join("display", "Movement Mana", "MovementMana4.png")),
        pygame.image.load(os.path.join("display", "Movement Mana", "MovementMana3.png")),
        pygame.image.load(os.path.join("display", "Movement Mana", "MovementMana2.png")),
        pygame.image.load(os.path.join("display", "Movement Mana", "MovementMana1.png")),
        pygame.image.load(os.path.join("display", "Movement Mana", "MovementMana.png")),
        ]

        self.exp_image = [
        pygame.image.load(os.path.join("display", "XPBAR", "xpbar_1.png")),
        pygame.image.load(os.path.join("display", "XPBAR", "xpbar_2.png")),
        pygame.image.load(os.path.join("display", "XPBAR", "xpbar_3.png")),
        pygame.image.load(os.path.join("display", "XPBAR", "xpbar_4.png")),
        pygame.image.load(os.path.join("display", "XPBAR", "xpbar_5.png")),
        pygame.image.load(os.path.join("display", "XPBAR", "xpbar_6.png")),
        pygame.image.load(os.path.join("display", "XPBAR", "xpbar_7.png")),
        pygame.image.load(os.path.join("display", "XPBAR", "xpbar_8.png")),
        pygame.image.load(os.path.join("display", "XPBAR", "xpbar_9.png")),
        pygame.image.load(os.path.join("display", "XPBAR", "xpbar_10.png")),
        pygame.image.load(os.path.join("display", "XPBAR", "xpbar_M.png"))
        ]

        self.pxe_image = [
        pygame.image.load(os.path.join("display", "PxBar", "xpbar_1.png")),
        pygame.image.load(os.path.join("display", "PxBar", "xpbar_2.png")),
        pygame.image.load(os.path.join("display", "PxBar", "xpbar_3.png")),
        pygame.image.load(os.path.join("display", "PxBar", "xpbar_4.png")),
        pygame.image.load(os.path.join("display", "PxBar", "xpbar_5.png")),
        pygame.image.load(os.path.join("display", "PxBar", "xpbar_6.png")),
        pygame.image.load(os.path.join("display", "PxBar", "xpbar_7.png")),
        pygame.image.load(os.path.join("display", "PxBar", "xpbar_8.png")),
        pygame.image.load(os.path.join("display", "PxBar", "xpbar_9.png")),
        pygame.image.load(os.path.join("display", "PxBar", "xpbar_10.png")),
        pygame.image.load(os.path.join("display", "PxBar", "xpbar_M.png"))
        ]

        self.Sword_image = [
            pygame.image.load(os.path.join("display", "Loading Sword", "swordgif1.png")),
            pygame.image.load(os.path.join("display", "Loading Sword", "swordgif2.png")),
            pygame.image.load(os.path.join("display", "Loading Sword", "swordgif3.png")),
        ]

        self.missile_image_up = pygame.image.load(os.path.join("display", "Arrows", "Arrow_up.png"))
        self.missile_image_down = pygame.image.load(os.path.join("display", "Arrows", "Arrow_down.png"))
        self.missile_image_left = pygame.image.load(os.path.join("display", "Arrows", "Arrow_left.png"))
        self.missile_image_right = pygame.image.load(os.path.join("display", "Arrows", "Arrow_right.png"))
        self.npc_image1 = pygame.image.load(os.path.join("display", "Eggefant", "eggefant.png"))
        self.npc_image2 = pygame.image.load(os.path.join("display", "Eggefant", "eggefant2.png"))
        self.wall_image = pygame.image.load(os.path.join("display", "Wall.png"))
        self.background_image = pygame.image.load(os.path.join("display", "Background00%s.png" % self.randomizer() )) 
        self.Menu_image = pygame.image.load(os.path.join("display", "Menu.png"))
        self.gamestate = -1
        return

    def paint_pregame(self, surface, control):
        """
        Draws the display before the user selects the game type.
        """
        if self.gamestate != 0:
            self.gamestate = 0
            pygame.mixer.music.load("load.mp3")
            pygame.mixer.music.set_volume(.20)
            pygame.mixer.music.play(-1)
        # background
        rect = pygame.Rect(0, 0, self.width, self.height)
        surface.blit(self.Menu_image, (0,0))
        # text message in center of screen
        s = "Archers Arena"
        self.draw_text_center(surface, s, self.text_color,
                              175, 250,
                              self.title_font)
        s = "Press 's' for single player"
        self.draw_text_center(surface, s, self.text_color,
                              175, 270 + 3*self.font_size/2,
                              self.font)
        s = "Press 'd' for dual player"
        self.draw_text_center(surface, s, self.text_color,
                              175, 280 + 6*self.font_size/2,
                              self.font)
        s = "Press 't' for tournament"
        self.draw_text_center(surface, s, self.text_color,
                              175, 290 + 9*self.font_size/2,
                              self.font)
        s = "Press 'esc' to quit"
        self.draw_text_center(surface, s, self.text_color,
                              175, 300 + 12*self.font_size/2,
                              self.font)

        return
        
    def paint_waiting_for_game(self, surface, engine, control):
        """
        Draws the display after user selects the game type, before the game begins.
        This is usually a brief period of time, while waiting for an opponent
        to join the game.
        """
        # background
        rect = pygame.Rect(0, 0, self.width, self.height)
        surface.fill(self.background_color, rect)
        if self.image_count <= 4:
            surface.blit(self.Sword_image[0], (0, 0))
            self.image_count += 1
        elif 4 < self.image_count <= 9:
            self.image_count += 1
            surface.blit(self.Sword_image[1], (0, 0))
        elif 9 < self.image_count <= 14:
            self.image_count += 1
            surface.blit(self.Sword_image[2], (0, 0))
        if self.image_count > 14:
            self.image_count = 0
        # text message in center of screen
        s = "Locating a worthy opponent..."
        self.draw_text_center(surface, s, self.text_color,
                              self.width/2, self.height/2,
                              self.font)
        return

    def paint_game(self, surface, engine, control):
        """
        Draws the display after the game starts.
        """
        if self.gamestate != 1:
            self.gamestate = 1
            pygame.mixer.music.stop()
            pygame.mixer.music.load("fight.mp3")
            pygame.mixer.music.play(-1)
        # background
        rect = pygame.Rect(0, 0, self.width, self.height)
        surface.fill(self.background_color, rect)
        surface.blit(self.background_image, (0,0))
            
        # draw each object
        objs = engine.get_objects()
        for key in objs:
            obj = objs[key]
            if obj.is_wall():
                self.paint_wall(surface, engine, control, obj)
            elif obj.is_npc():
                self.paint_npc(surface, engine, control, obj)
            elif obj.is_missile():
                self.paint_missile(surface, engine, control, obj)
            elif obj.is_player():
                self.paint_player(surface, engine, control, obj)
            else:
                print "Unexpected object type: %s" % (str(obj.__class__))
                
        # draw game data
        if control.show_info:
            self.paint_game_status(surface, engine, control)
        return

        
    def paint_game_over(self, surface, engine, control):
        """
        Draws the display after the game ends.  This
        chooses to display the game, and add a game over
        message.
        """
        if self.gamestate != 2:
            self.gamestate = 2
            pygame.mixer.stop()
            pygame.mixer.music.load("end.mp3")
            pygame.mixer.music.play()
        rect = pygame.Rect(0, 0, self.width, self.height)
        surface.blit(self.Menu_image, (0,0))
        self.paint_game(surface, engine, control)

        if engine.get_opponent_name() == engine.get_winner_name():
            loser = engine.get_name()
        else:
            loser = engine.get_opponent_name()
        
        s = "%s" % (loser)
        self.draw_text_center(surface, s, self.text_color, int(self.width/2), int(self.height/2), self.font)
        return

    def process_event(self, surface, engine, control, event):
        """
        Should process the event and decide if it needs to be displayed, or heard.
        """
        import os
        if isinstance(event, MissileFireEvent):
            shot = pygame.mixer.Sound(os.path.join(os.getcwd(), "shot.wav"))
            shot.set_volume(.5)
            shot.play()
        if isinstance(event, MissileHitEvent):
            hit = pygame.mixer.Sound(os.path.join(os.getcwd(), "hit.wav"))
            hit.set_volume(.5)
            hit.play()
        if isinstance(event, MissileMisfireEvent):
            no_mp = pygame.mixer.Sound(os.path.join(os.getcwd(), "no_mp.mp3"))
            no_mp.set_volume(.5)
            no_mp.play()
        return

    # The following methods draw appropriate rectangles
    # for each of the objects, by type.
    # Most objects have an optional text display to
    # demonstrate how to send information from the control
    # to the display.
    def paint_wall(self, surface, engine, control, obj):
        """
        Draws walls.
        """
        rect = self.obj_to_rect(obj)
        surface.blit(self.wall_image, (obj.get_px(), obj.get_py()))
        return
        
    def paint_npc(self, surface, engine, control, obj):
        """
        Draws living NPCs.
        """
        if obj.is_alive():
            color = self.npc_color
            rect = self.obj_to_rect(obj)
            surface.blit(self.npc_image1, (obj.get_px(), obj.get_py()))
        return
        
    def paint_missile(self, surface, engine, control, obj):
        """
        Draws living missiles.
        """
        if obj.is_alive():
            rect = self.obj_to_rect(obj)
            if obj.get_dx() <= 0:
                    if abs(obj.get_dx()) > abs(obj.get_dy()):
                        #facing left
                        surface.blit(self.missile_image_left, (obj.get_px(), obj.get_py()))
                    else:
                        #facing up
                        surface.blit(self.missile_image_up, (obj.get_px(), obj.get_py()))
            elif abs(obj.get_dx()) > abs(obj.get_dy()):
                #facing right
                surface.blit(self.missile_image_right, (obj.get_px(), obj.get_py()))
            else:
                #facing down
                surface.blit(self.missile_image_down, (obj.get_px(), obj.get_py()))
        return
        
    def paint_player(self, surface, engine, control, obj):
        """
        Draws living players.
        My player is my opponent are in different colors
        """
        if obj.is_alive():
            rect = self.obj_to_rect(obj)
            if obj.get_oid() == engine.get_player_oid():
                color = self.player_color
                if obj.get_dx() < 0:
                    if abs(obj.get_dx()) <= abs(obj.get_dy()):
                        #left
                        if self.image_count <= 4:
                            surface.blit(self.player_image_leftidle, (obj.get_px(), obj.get_py()))
                            self.image_count += 1
                        elif 4 < self.image_count <= 9:
                            self.image_count += 1
                            surface.blit(self.player_image_left1, (obj.get_px(), obj.get_py()))
                        elif 9 < self.image_count <= 14:
                            self.image_count += 1
                            surface.blit(self.player_image_leftidle, (obj.get_px(), obj.get_py()))
                        elif 14 < self.image_count <= 19:
                            self.image_count += 1
                            surface.blit(self.player_image_left2, (obj.get_px(), obj.get_py()))
                        if self.image_count > 19:
                            self.image_count = 0
                    else:
                        #up
                        if self.image_count <= 5:
                            surface.blit(self.player_image_up1, (obj.get_px(), obj.get_py()))
                            self.image_count += 1
                        if self.image_count <= 10:
                            surface.blit(self.player_image_up2, (obj.get_px(), obj.get_py()))
                            self.image_count += 1
                        if self.image_count > 10:
                            surface.blit(self.player_image_upidle, (obj.get_px(), obj.get_py()))
                            self.image_count = 0
                elif obj.get_x() > 0:
                    if abs(obj.get_dx()) <= abs(obj.get_dy()):
                        #right
                        if self.image_count <= 4:
                            surface.blit(self.player_image_rightidle, (obj.get_px(), obj.get_py()))
                            self.image_count += 1
                        elif 4 < self.image_count <= 9:
                            self.image_count += 1
                            surface.blit(self.player_image_right1, (obj.get_px(), obj.get_py()))
                        elif 9 < self.image_count <= 14:
                            self.image_count += 1
                            surface.blit(self.player_image_rightidle, (obj.get_px(), obj.get_py()))
                        elif 14 < self.image_count <= 19:
                            self.image_count += 1
                            surface.blit(self.player_image_right2, (obj.get_px(), obj.get_py()))
                        if self.image_count > 19:
                            self.image_count = 0
                    else:
                        #down
                        if self.image_count <= 4:
                            surface.blit(self.player_image_downidle, (obj.get_px(), obj.get_py()))
                            self.image_count += 1
                        elif 4 < self.image_count <= 9:
                            self.image_count += 1
                            surface.blit(self.player_image_down1, (obj.get_px(), obj.get_py()))
                        elif 9 < self.image_count <= 14:
                            self.image_count += 1
                            surface.blit(self.player_image_downidle, (obj.get_px(), obj.get_py()))
                        elif 14 < self.image_count <= 19:
                            self.image_count += 1
                            surface.blit(self.player_image_down2, (obj.get_px(), obj.get_py()))
                        if self.image_count > 19:
                            self.image_count = 0
            else:
                color = self.opponent_color
                if obj.get_dx() <= 0:
                    if abs(obj.get_dx()) > abs(obj.get_dy()):
                        #facing left
                        if self.image_count <= 4:
                            surface.blit(self.opponent_image_leftidle, (obj.get_px(), obj.get_py()))
                            self.image_count += 1
                        elif 4 < self.image_count <= 9:
                            self.image_count += 1
                            surface.blit(self.opponent_image_left1, (obj.get_px(), obj.get_py()))
                        elif 9 < self.image_count <= 14:
                            self.image_count += 1
                            surface.blit(self.opponent_image_leftidle, (obj.get_px(), obj.get_py()))
                        elif 14 < self.image_count <= 19:
                            self.image_count += 1
                            surface.blit(self.opponent_image_left2, (obj.get_px(), obj.get_py()))
                        if self.image_count > 19:
                            self.image_count = 0
                    else:
                        #facing up
                        if self.image_count <= 5:
                            surface.blit(self.opponent_image_up1, (obj.get_px(), obj.get_py()))
                            self.image_count += 1
                        if self.image_count <= 10:
                            surface.blit(self.opponent_image_up2, (obj.get_px(), obj.get_py()))
                            self.image_count += 1
                        if self.image_count > 10:
                            surface.blit(self.opponent_image_upidle, (obj.get_px(), obj.get_py()))
                            self.image_count = 0
                            
                elif abs(obj.get_dx()) > abs(obj.get_dy()):
                    #facing right
                    if self.image_count <= 4:
                        surface.blit(self.opponent_image_rightidle, (obj.get_px(), obj.get_py()))
                        self.image_count += 1
                    elif 4 < self.image_count <= 9:
                        self.image_count += 1
                        surface.blit(self.opponent_image_right1, (obj.get_px(), obj.get_py()))
                    elif 9 < self.image_count <= 14:
                        self.image_count += 1
                        surface.blit(self.opponent_image_rightidle, (obj.get_px(), obj.get_py()))
                    elif 14 < self.image_count <= 19:
                        self.image_count += 1
                        surface.blit(self.opponent_image_right2, (obj.get_px(), obj.get_py()))
                    if self.image_count > 19:
                        self.image_count = 0
                else:
                    #facing down
                    if self.image_count <= 5:
                        surface.blit(self.opponent_image_down1, (obj.get_px(), obj.get_py()))
                        self.image_count += 1
                    if self.image_count <= 10:
                        surface.blit(self.opponent_image_down2, (obj.get_px(), obj.get_py()))
                        self.image_count += 1
                    if self.image_count > 10:
                        surface.blit(self.opponent_image_downidle, (obj.get_px(), obj.get_py()))
                        self.image_count = 0
                

        return

    def get_health_image(self, health):
        health = health / 3.0
        # I think this works, please forgive me.
        # Dear self,
        #    I was tired and they made me write this.
        # I apologize.
        #    - The code monkey nutz
        return self.health_images[int(math.ceil(health))]

    def get_exp_image(self, exp):
        exp = exp / 4.5
        return self.exp_image[int(math.ceil(exp))]

    def get_pxe_image(self, exp):
        exp = exp / 4.5
        return self.exp_image[int(math.ceil(exp))]

    def get_mana_image(self, mana):
        if mana > 10.0:
            mana = 10.0
        return self.mana_image[int(math.ceil(mana))]
        

    def get_arrow_image(self, arrows):
        if arrows > 10.0:
            arrows = 10.0
        return self.arrow_images[int(math.ceil(arrows))]

    def paint_game_status(self, surface, engine, control):
        """
        This method displays some text in the bottom strip
        of the screen.  You can make it do whatever you want,
        or nothing if you want.
        """

        # display my stats
        oid = engine.get_player_oid()
        if oid > 0: 
            obj = engine.get_object(oid)
            if obj:
                s = "Me: %s  HP: %.1f  XP: %.1f Mv: %.1f Ms: %.1f" % \
                    (engine.get_name(),
                     obj.get_health(),
                     obj.get_experience(),
                     obj.get_move_mana(),
                     obj.get_missile_mana())
                #position_x = 20
                #position_y = self.height - STATUS_BAR_HEIGHT + 3 * self.font_size / 2
                #self.draw_text_left(surface, s, self.text_color, position_x, position_y, self.font)
                image = self.get_health_image(obj.get_health())
                surface.blit(image, (0, surface.get_height() - 50))
                image = self.get_arrow_image(obj.get_missile_mana())
                surface.blit(image, (surface.get_width() / 2 - 90, surface.get_height() - 20))
                image = self.get_mana_image(obj.get_move_mana())
                surface.blit(image, (surface.get_width() / 2 -150, surface.get_height() -50))
                image = self.get_exp_image(obj.get_experience())
                surface.blit(image, (surface.get_width() / 2 -210, surface.get_height() -60))
                                
        # display opponent's stats
        oid = engine.get_opponent_oid()
        if oid > 0: 
            obj = engine.get_object(oid)
            if obj:
                s = "Opponent: %s  HP: %.1f  XP: %.1f Mv: %.1f Ms: %.1f" % \
                    (engine.get_opponent_name(),
                     obj.get_health(),
                     obj.get_experience(),
                     obj.get_move_mana(),
                     obj.get_missile_mana())
                #position_x = 20
                #position_y = self.height - STATUS_BAR_HEIGHT + 6 * self.font_size / 2
                #self.draw_text_left(surface, s, self.text_color, position_x, position_y, self.font)
                image = self.get_health_image(obj.get_health())
                surface.blit(image, (surface.get_width() - 50, surface.get_height() - 50))
                image = self.get_arrow_image(obj.get_missile_mana())
                surface.blit(image, (surface.get_width() / 2 + 10, surface.get_height() - 20))
                image = self.get_mana_image(obj.get_move_mana())
                surface.blit(image, (surface.get_width() / 2 + 100, surface.get_height() - 50))
                image = self.get_pxe_image(obj.get_experience())
                surface.blit(image, (surface.get_width() / 2 +150, surface.get_height() -60))
        return

