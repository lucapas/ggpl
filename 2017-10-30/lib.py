from larlib import *
def hex_material(color, light, trasparence):

    def hex_to_rgb(value):
        value = value.lstrip('#')
        lv = len(value)
        return map(lambda x: x/255., list(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3)))

    params = hex_to_rgb(color) + [.1] + \
             hex_to_rgb(light) + [trasparence] +\
             hex_to_rgb(light) + [.1] +\
             hex_to_rgb("#000000") + [.1] +\
             [100]

    return MATERIAL(params)



def shelf(x,y,z):
    return STRUCT([CUBOID([x,y,z*0.05]),CUBOID([x,y*0.05,z]),CUBOID([x*0.05,y,z]),T(1)(x*0.95)(CUBOID([x*0.05,y,z])),T(3)(z*0.95)(CUBOID([x,y,z*0.05]))])

def table(width,depth,height):
    plane=CUBOID([width,depth*1.5,height*.1])
    legs=CUBOID([width*.1,depth*.1,height*.8])
    return STRUCT([legs,T(3)(height*.8)(plane),T([1,2])([width*.9,depth*1.4])(legs),T(1)(width*.9)(legs),T(2)(depth*1.4)(legs)])
