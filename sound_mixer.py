import pygame

class SoundMixer():

    def __init__(self):
        # Setup for sounds. Defaults are good.
        #pygame.mixer.init() always call before pygame.init() when customization needed
        pass
    
    """ -1 means loop infinitely"""
    def play_sound(self, sound, loop_count: int):
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play(loops =- 1)

    # def custom():
    #     collision_sound = pygame.mixer.Sound("Collision.ogg")
    #     collision_sound.play()    

    def shutdown(self):
        pygame.mixer.music.stop()
        pygame.mixer.musit.quit()
