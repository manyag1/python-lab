def check_point_position(circle_x, circle_y, radius, point_x, point_y):
    
    distance = math.sqrt(math.pow(point_x - circle_x, 2) + math.pow(point_y - circle_y, 2))
    
    
    if distance < radius:
        return "Inside the circle"
    elif distance == radius:
        return "On the circle"
    else:
        return "Outside the circle"
