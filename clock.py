from nanoleaf import Aurora
from leaf_details import ip_addr, token
from datetime import datetime
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
    "command" : "display",
    "animType": "static",
    "animData": animData}
    lights.effect_set_raw(effect_data)

def update_clock():
    scaled_sec = round(datetime.now().second / 60 * 255)
    send(get_animdata_to_color_all(scaled_sec, 0, 255-scaled_sec, 0, 0))