from turtle import * #i kwon i cant run turtle here but i have a question
from math import pi, sin, cos, sqrt, acos, asin, atan2
def deformation(p, centre, rayon):
    """ Calcul des coordonnées d'un point suite à la déformation engendrée par la sphère émergeante
        Entrées :
          p : coordonnées (x, y, z) du point du dalage à tracer (z = 0) AVANT déformation
          centre : coordonnées (X0, Y0, Z0) du centre de la sphère
          rayon : rayon de la sphère
        Sorties : coordonnées (xprim, yprim, zprim) du point du dallage à tracer APRÈS déformation
    """
    x, y, z = p
    xprim, yprim, zprim = x, y, z
    xc, yc, zc = centre
    if rayon**2 > zc**2:
        zc = zc if zc <= 0 else -zc
        r = sqrt(
            (x - xc) ** 2 + (y - yc) ** 2)                  # distance horizontale depuis le point à dessiner jusqu'à l'axe de la sphère
        rayon_emerge = sqrt(rayon ** 2 - zc ** 2)           # rayon de la partie émergée de la sphère
        rprim = rayon * sin(acos(-zc / rayon) * r / rayon_emerge)
        if 0 < r <= rayon_emerge:                 # calcul de la déformation dans les autres cas
            xprim = xc + (x - xc) * rprim / r               # les nouvelles coordonnées sont proportionnelles aux anciennes
            yprim = yc + (y - yc) * rprim / r
        if r <= rayon_emerge:
            beta = asin(rprim / rayon)
            zprim = zc + rayon * cos(beta)
            if centre[2] > 0:
                zprim = -zprim
    return (xprim, yprim, zprim)
def hexagone(longueur,col,centre,rayon):
    (col1,col2,col3)=col
    (xc, yc, zc) = centre
    A = [0,pi / 3,(2 * pi) / 3,(-2 * pi) / 3,-pi/3,0,(-2 * pi) / 3,pi,(2 * pi) / 3]
    n = position() #position du centre
    c=deformation((n[0], n[1],0),centre,rayon) #calcule deformation du centre
    up()
    goto(c[0],c[1])
    down()
    for i in range(len(A)): #boucle qui permet de calculer les 6 point de l'hexagone
        x = (longueur * cos(A[i]))+n[0]
        a = (longueur * sin(A[i]))+n[1]
        p=deformation((x,a,0),centre,rayon)#ajoute z=0,
        goto(p[0], p[1])
        if i==0: #debut 1 er losange
            fillcolor(col1)
            begin_fill()
        if i==2:
            goto(c[0], c[1])
            end_fill() #fin
            fillcolor(col2) #debut 2 eme losange
            begin_fill()
        if i==5:
            goto(c[0], c[1])
            end_fill()
            fillcolor(col3) #debut 3 eme losange
            begin_fill()
        if i==8:
            goto(c[0], c[1])
            end_fill() #fin
def pavage():
    inf_gauche=int(input('valeur'))
    sup_droit=int(input('valeur'))
    longueur=int(input('valeur'))
    col1=input('r')
    col2=input('g')
    col3=input('g')
    col=(col1,col2,col3)
    xc=int(input('g'))
    yc=int(input('g'))
    zc=int(input('g'))
    centre=(xc,yc,zc)
    rayon=int(input('g'))

    up()
    y = longueur * sin((2 * pi) / 3)  #
    x = longueur * cos((2 * pi) / 3)
    f = longueur * cos((-2 * pi) / 3)
    g = longueur * sin((-2 * pi) / 3)
    goto(x, y)
    n = position()
    goto(f, g)
    A = distance(n)
    down()
    z = inf_gauche
    w = inf_gauche
    y = inf_gauche + (A) / 2
    k = 0
    while z < sup_droit:  # calcule cordonée
        up()
        w, z = z, z + A  # cordonné ligne paire y
        k, y = y, y + A  # cordonné ligne impaire y
        x = inf_gauche
        f = inf_gauche + (1.5 * 20)
        down()
        while x < sup_droit:  # ligne paire
            up()
            goto(x, w)
            x = x + (longueur * 3)
            down()
            hexagone(longueur, col, centre, rayon)
        while f < sup_droit:  # ligne impaire
            up()
            goto(f, k)
            f = f + (longueur * 3)
            down()
            hexagone(longueur, col, centre, rayon)
pavage()
exitonclick()