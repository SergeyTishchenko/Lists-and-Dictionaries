import random

def solar_system():
    return {'Mercury': 57.9,
            'Venus': 67.2,
            'Earth': 149.6,
            'Mars': 227.9,
            'Jupiter': 778.3,
            'Saturn': 1427.0,
            'Uranus': 2871.0,
            'Neptune': 4497.1,
            }


if __name__ == '__main__':
    dic = solar_system()
    planet = random.choice(dic.keys())
    distance = dic.get(planet)
    print "Planet {name} is about {dist} million kilometers from the sun".format(name=str(planet), dist=str(distance))
