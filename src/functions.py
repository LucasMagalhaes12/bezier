def lerp(a, b, t):
    return a * (1-t) + b * t


def bezier(a:int, b:int, c:int, d:int, t:int):
    e = lerp(a, b, t)
    f = lerp(b, c, t)
    g = lerp(c, d, t)

    h = lerp(e, f, t)
    i = lerp(f, g, t)
    
    return lerp(h, i, t)

