
def calculate_food_points(protein=0.0,
                          carbs=0.0,
                          fat=0.0,
                          fiber=0.0,
                          alcohol=0.0,
                          sugar_alcohol=0.0):
    points = (
        (float(protein) / 10.9375)
        + (float(carbs) / 9.2105)
        + (float(fat) / 3.8889)
        + (float(alcohol) / 3.0147)
        - (float(fiber) / 12.5)
        - (float(sugar_alcohol) / 23.0263)
    )
    if points > 0:
        return int(round(points))
    else:
        return 0

