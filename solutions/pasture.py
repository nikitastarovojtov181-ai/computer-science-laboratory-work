def pasture_area(wire, w):
    if w <= 0 or w*2 > wire:
        return 0
    l = (wire - 2*w)/3
    return w * l

def best_pasture(wire):
    w = wire/4
    l = (wire - 2*w)/3
    area = w * l
    return (w, l, area)

if __name__ == '__main__':

    print(pasture_area(100, 25))
    print(pasture_area(100, 10))
    print(pasture_area(100, 50))

    print(best_pasture(100))
    print(best_pasture(60))
    print(best_pasture(12))
