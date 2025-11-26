import re

with open(".\\2015\\14\\input.txt", "r", encoding="utf-8") as file:
    inputs = file.read()

def lines_parser(lines):
    re_pattern = re.compile(r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.")
    re_matches = re_pattern.findall(lines)

    deers = {}
    for match in re_matches:
        name = match[0]
        speed = int(match[1])
        fly_time = int(match[2])
        rest_time = int(match[3])
        deers[name] = {
            "speed": speed,
            "fly_time": fly_time,
            "rest_time": rest_time,
            "current_state": "flying",
            "time_in_state": 0,
            "distance": 0,
            "points": 0
        }

    return deers

deers = lines_parser(inputs)

for second in range(2503):
    for deer in deers.values():
        if deer["current_state"] == "flying":
            deer["distance"] += deer["speed"]
            deer["time_in_state"] += 1
            if deer["time_in_state"] == deer["fly_time"]:
                deer["current_state"] = "resting"
                deer["time_in_state"] = 0
        else:  # resting
            deer["time_in_state"] += 1
            if deer["time_in_state"] == deer["rest_time"]:
                deer["current_state"] = "flying"
                deer["time_in_state"] = 0

    # Award points to the leading deer(s)
    max_distance_this_second = max(deer["distance"] for deer in deers.values())
    for deer in deers.values():
        if deer["distance"] == max_distance_this_second:
            deer["points"] += 1

print(max(deer["points"] for deer in deers.values()))