def check_violation(vehicle_bbox, lane_line_y):
    x1, y1, x2, y2 = vehicle_bbox

    if y2 > lane_line_y:
        return True
    return False