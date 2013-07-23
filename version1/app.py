import pyglet
import resources, load

window_width = 800
window_height = 600



lives = load.player_lives(5)
asteroids = load.asteroids(3, resources.player_ship.position)

game_window = pyglet.window.Window(window_width, window_height)
game_objects = [resources.player_ship] + asteroids


@game_window.event
def on_draw():
	game_window.clear()
	resources.main_batch.draw()

def update(dt):
    for obj in game_objects:
        obj.update(dt)


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()