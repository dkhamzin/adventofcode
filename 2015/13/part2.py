import re
import itertools

with open(".\\2015\\13\\input.txt", "r", encoding="utf-8") as file:
    inputs = file.read()

def lines_parser(lines):
    person_pairs = {}
    people = set()
    people.add("Me")  # Add yourself to the list of people
    re_pattern = re.compile(r"(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+).")
    
    for line in lines:
        match = re_pattern.match(line)
        if match:
            person1, gain_lose, units, person2 = match.groups()
            delta = int(units) if gain_lose == "gain" else -int(units)
            person_pairs[(person1, person2)] = delta
            people.update([person1, person2])
    
    return person_pairs, list(people)

def total_happiness(arrangement, person_pairs):
    total = 0
    n = len(arrangement)
    for i in range(n):
        left = arrangement[i]
        right = arrangement[(i + 1) % n]
        total += person_pairs.get((left, right)) if person_pairs.get((left, right)) is not None else 0
        total += person_pairs.get((right, left)) if person_pairs.get((right, left)) is not None else 0
    return total

def find_optimal_seating(lines):
    person_pairs, people = lines_parser(lines)
    best_score = 0
    best_arrangement = None
    
    for perm in itertools.permutations(people):
        score = total_happiness(perm, person_pairs)
        if score > best_score:
            best_score = score
            best_arrangement = perm
    
    return best_arrangement, best_score

input_lines = inputs.splitlines()
arrangement, score = find_optimal_seating(input_lines)
print("Best arrangement:", arrangement)
print("Total happiness:", score)
