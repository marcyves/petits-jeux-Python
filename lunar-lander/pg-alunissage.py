from src.constants import MAIN_WIN_WIDTH, MAIN_WIN_HEIGHT
from src.InfoBox import InfoBox
from src.Menus import StartMenu, OptionsMenu, GenericActions

class StartScreen:
    def __init__(self, screen):
        self.screen = screen
        self.menu_screen = self.screen.copy()

        # Start screen loop
        bg_image = pg.image.load('imgs/interface/main_menu_background.jpg').convert_alpha()
        self.background = pg.transform.scale(bg_image, screen.get_size())

        # Creating menu
        self.active_menu = StartScreen.create_menu()
        self.background_menus = []

        # Memorize if a game is currently being performed
        self.level = None

        self.levels = [0, 1]
        self.level_id = None

        # Load current saved parameters
#        self.load_options()

        self.exit = False

    @staticmethod
    def create_menu():
        entries = [[{'name': 'Nouvelle partie', 'id': StartMenu.NEW_GAME}], 
                   [{'name': 'Options', 'id': StartMenu.OPTIONS}], [{'name': 'Terminer', 'id': StartMenu.EXIT}]]

        for row in entries:
            for entry in row:
                entry['type'] = 'button'

        return InfoBox("Alunissage", StartMenu,
                       "imgs/interface/PopUpMenu.png", entries, START_MENU_WIDTH)

    def motion(self, pos):
        if self.level is None:
            self.active_menu.motion(pos)
        else:
            self.level.motion(pos)

    def click(self, button, pos):
        if self.level is None:
            if button == 1:
                self.execute_action(self.active_menu.type, self.active_menu.click(pos))
        else:
            self.level.click(button, pos)
        return self.exit

    def update_state(self):
        if self.level:
            status = self.level.update_state()
            if status is Status.ENDED_VICTORY:
                self.level_id += 1
                if self.level_id in self.levels:
                    team = self.level.passed_players
                    for player in team:
                        # Players are fully restored between level
                        player.healed(player.hp_max)
                        # Reset player's state
                        player.new_turn()
                    self.play(StartScreen.load_level(self.level_id, team))
                else:
                    # TODO: Game win dialog?
                    self.screen = pg.display.set_mode((self.menu_screen.get_width(), self.menu_screen.get_height()))
                    self.level = None
            elif status is Status.ENDED_DEFEAT:
                self.screen = pg.display.set_mode((self.menu_screen.get_width(), self.menu_screen.get_height()))
                self.level = None

    def display(self):
        if self.level:
            self.screen.fill(BLACK)
            self.level.display(self.screen)
        else:
            self.screen.blit(self.background, (0, 0))
            for menu in self.background_menus:
                if menu[1]:
                    menu[0].display(self.screen)
            if self.active_menu:
                self.active_menu.display(self.screen)

    def button_down(self, button, pos):
        if self.level is not None:
            self.level.button_down(button, pos)

    def execute_action(self, menu_type, action):
        if not action:
            return
        method_id = action[0]
        args = action[1]

        # Test if the action is a generic one (according to the method_id)
        # Close menu : Active menu is closed
        if method_id is GenericActions.CLOSE:
            self.active_menu = None
            if self.background_menus:
                self.active_menu = self.background_menus.pop()[0]
            return

        if menu_type is StartMenu:
            self.main_menu_action(method_id, args)
        elif menu_type is OptionsMenu:
            self.options_menu_action(method_id, args)
        else:
            print("Unknown menu... : ", str(menu_type))


def show_fps(win, inner_clock, font):
    fps_text = font.render("FPS: " + str(round(inner_clock.get_fps())), True, (255, 255, 0))
    win.blit(fps_text, (2, 2))


if __name__ == "__main__":
    import pygame as pg
    from src.constants import *
    import src.fonts as fonts

    pg.init()

    # Load fonts
    fonts.init_fonts()

    # Window parameters
    pg.display.set_caption("Alunissage")
    screen = pg.display.set_mode((MAIN_WIN_WIDTH, MAIN_WIN_HEIGHT))

    clock = pg.time.Clock()

    start_screen = StartScreen(screen)

    quit_game = False
    while not quit_game:

        for e in pg.event.get():
            if e.type == pg.QUIT:
                quit_game = True
            elif e.type == pg.MOUSEMOTION:
                start_screen.motion(e.pos)
            elif e.type == pg.MOUSEBUTTONUP:
                if e.button == 1 or e.button == 3:
                    quit_game = start_screen.click(e.button, e.pos)
            elif e.type == pg.MOUSEBUTTONDOWN:
                if e.button == 1 or e.button == 3:
                    start_screen.button_down(e.button, e.pos)
        start_screen.update_state()
        start_screen.display()
        show_fps(screen, clock, fonts.fonts['FPS_FONT'])
        pg.display.update()
        clock.tick(60)
    raise SystemExit
