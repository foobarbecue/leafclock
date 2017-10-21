from nanoleaf import Aurora
from leaf_details import ip_addr, token
from datetime import datetime
from time import sleep
from scipy.interpolate import interp1d

lights = Aurora(ip_addr, token)
ids = [panel['panelId'] for panel in lights.panel_positions]


def get_animdata_to_color_all(r, g, b, w, t):
    num_frames = "1 "
    panel_frames = [" ".join(map(str, [id, num_frames, r, g, b, w, t])) for id in ids]
    num_panels = str(len(ids))
    return num_panels + " " + " ".join(panel_frames)


def send(animData):
    print(animData)
    effect_data = {
        "command": "display",
        "animType": "static",
        "animData": animData}
    lights.effect_set_raw(effect_data)


def time_to_colors(leaf_time):
    leaf_time = leaf_time or datetime.now()
    scaled_sec = round(leaf_time.second / 60 * 255)
    seconds_color = [scaled_sec, 0, 255 - scaled_sec, 0, 0]

    scaled_mins = round(leaf_time.minute / 60 * 255)
    minutes_color = [scaled_mins, 0, 255 - scaled_mins, 0, 0]

    scaled_hours = round(leaf_time.hour / 24 * 255)
    hours_color = [scaled_hours, 0, 255 - scaled_hours, 0, 0]
    return {'hours': hours_color, 'minutes': minutes_color, 'seconds': seconds_color}


def update_clock():
    colors = time_to_colors(datetime.now())
    send(get_animdata_to_color_all(*colors['seconds']))

while True:
    update_clock()
    sleep(1)