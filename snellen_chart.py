import math

d = float(input("Enter the distance in metres: "))

def snellenLetter(distance):
    
    angle = math.tan(0.084)
    height = distance*angle
    return str(height) + " mm"

print(snellenLetter(d))
