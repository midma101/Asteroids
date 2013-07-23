import pyglet
from game import resources, load, player

window_width = 800
window_height = 600

main_batch = pyglet.graphics.Batch()

game_window = pyglet.window.Window(window_width, window_height)

score_label = pyglet.text.Label(text="Score: 0", x=10, y=575, batch=main_batch)
level_label = pyglet.text.Label(text="Midma's Asteroid Fun", 
                                x=400, y=575, anchor_x='center', batch=main_batch)


player_ship = player.Player(x=400, y=300, batch=main_batch)
lives = load.player_lives(5, batch=main_batch)



asteroids = load.asteroids(3, player_ship.position, main_batch)
game_objects = [player_ship] + asteroids

game_window.push_handlers(player_ship.key_handler)


@game_window.event
def on_draw():
	
	game_window.clear()
	main_batch.draw()

def update(dt):
    for obj in game_objects:
        obj.update(dt)


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()