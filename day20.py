from collections import defaultdict
from dataclasses import dataclass
from heapq import heapify, heappop, heappush
import re
from typing import List

Vector = List[int]

@dataclass
class Particle:
    p: Vector
    v: Vector
    a: Vector

    def update(self):
        for i in range(3):
            self.v[i] += self.a[i]
            self.p[i] += self.v[i]

        return abs(self.p[0]) + abs(self.p[1]) + abs(self.p[2])

def read_data(filename="data/input20.data"):
    with open(filename) as f:
        return f.read().splitlines()


def parse_data(lines):
    particles = []
    for line in lines:
        ints = [int(n) for n in re.findall(r"-?\d+", line)]
        particles.append(
            Particle(
                p = ints[:3],
                v = ints[3:6],
                a = ints[6:]
            )
        )

    return particles

if __name__ == "__main__":
    data = read_data()
    particles = parse_data(data)

    for tick in range(1000):
        distances = []
        for i, p in enumerate(particles):
            d = p.update()
            if tick == 999:
                heappush(distances, (d, i))

        if tick == 999:
            best = heappop(distances)
            print(best[1])

    soup = defaultdict(list)
    for particle in parse_data(data):
        soup[tuple(particle.p)].append(particle)

    # Part 2 -- no particular cleverness, just brute it out.
    # Converges very quickly.
    tick = 0
    while True:
        new_soup = defaultdict(list)
        for _, particle_list in soup.items():
            particle = particle_list[0]
            particle.update()
            new_soup[tuple(particle.p)].append(particle)

        soup = defaultdict(list)
        for pos, particles in new_soup.items():
            if len(particles) == 1:
                soup[tuple(pos)].append(particles[0])

        tick += 1

        if tick > 50:
            print(len(soup))
            break
