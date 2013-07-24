import pyglet
from game import resources, load, player, asteroid

window_width = 800
window_height = 600

main_batch = pyglet.graphics.Batch()
player_ship = player.Player(x=400, y=300, batch=main_batch)

game_window = pyglet.window.Window(window_width, window_height)

score_label = pyglet.text.Label(text="Score: "+str(player_ship.current_score), x=10, y=575, batch=main_batch)
level_label = pyglet.text.Label(text="Midma's Asteroid Fun", 
                                x=400, y=575, anchor_x='center', batch=main_batch)



lives = load.player_lives(5, batch=main_batch)



asteroids = load.asteroids(3, player_ship.position, main_batch)
game_objects = [player_ship] + asteroids

game_window.push_handlers(player_ship.key_handler)


@game_window.event
def on_draw():
	
	game_window.clear()
	main_batch.draw()
	score_label.draw()

def update(dt):
	
	
    for i in xrange(len(game_objects)):
    	for j in xrange(i+1, len(game_objects)):
    		obj_1 = game_objects[i]
    		obj_2 = game_objects[j]
    		if not obj_1.dead and not obj_2.dead:
    			if obj_1.collides_with(obj_2):
    			    obj_1.handle_collision_with(obj_2)
    			    obj_2.handle_collision_with(obj_1)
    to_add = []

    for obj in game_objects:
        obj.update(dt)
        to_add.extend(obj.new_objects)
        obj.new_objects = []
    for to_remove in [obj for obj in game_objects if obj.dead]:
    	
    	to_remove.delete()
    	game_objects.remove(to_remove)
    player_ship.current_score = player_ship.current_score + 10
    game_objects.extend(to_add)
    print player_ship.current_score


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()