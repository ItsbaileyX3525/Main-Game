from ursina import *
from ursina.prefabs.first_person_controller import *
import random as ra
app=Ursina()
player=FirstPersonController()
ground=Entity(model='plane', collider='box',origin_y=-.01, scale=64, texture='grass', texture_scale=(4,4))
sus=Entity()
class monkey(Entity):
    def __init__(self,**kwargs):
        super().__init__(parent=sus, model='cube',texture='noice.mp4', scale=1, collider='box',y=1, **kwargs)

example=[monkey(x=ra.uniform(1,4)*ra.uniform(1.5,8),z=ra.uniform(1,3)*ra.uniform(1.5,8)) in range(1)]
app.run()