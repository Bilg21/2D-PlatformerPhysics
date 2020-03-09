import configparser

SETTINGS_FILE = 'settings.ini'
DIR_SPRITES = "assets/sprites"
DIR_LEVELS = "assets/levels"

class GlobalSettings():

    TARGET_FPS = 0 # 0 unlimited
    SCREEN_WIDTH = 1024
    SCREEN_HEIGHT = 768

    config = configparser.ConfigParser()

    def __init__(self):
        self.load_settings_from_file()

    def load_settings_from_file(self):
        self.config.read(SETTINGS_FILE)

        self.TARGET_FPS = int(self.config.get('Basic Game Settings', 'TARGET_FPS'))
        self.SCREEN_WIDTH = int(self.config.get('Basic Game Settings', 'SCREEN_WIDTH'))
        self.SCREEN_HEIGHT = int(self.config.get('Basic Game Settings', 'SCREEN_HEIGHT'))

    def save_settings_to_file(self):
        with open(SETTINGS_FILE, 'r') as setting_file:
            self.config.write(setting_file)
                