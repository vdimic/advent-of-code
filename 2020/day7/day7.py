#!/usr/bin/env python3

def parse(line):
    # remove unnecessary bits
    line = line.replace(' bags', '').replace(' bag','').replace('.','').replace(',','')
    tokens = line.split()
    print(tokens)
    container_color = ' '.join([tokens[0], tokens[1]])
    #tokens[2] is 'contains'
    #tokens[3] onwards are useful
    contained_colors = []
    index = 3
    while index < len(tokens):
        #tokens[index] is number
        if tokens[index] == 'no':
            break;
        else:
            contained_color = ' '.join([tokens[index+1], tokens[index+2]])
            contained_colors.append(contained_color)
        index += 3
    return container_color, contained_colors

class ContainedIn:
    def __init__(self):
        self.c = {}

    def add_container_contained(self, container, contained):
        for inner in contained:
            if inner in self.c:
                self.c[inner].append(container)
            else:
                self.c[inner] = [container]

    def get_containers(self, contained):
        if contained in self.c:
            return self.c[contained]
        else:
            return []

    def get_num_containers(self, contained):
        containers = self.get_containers(contained)
        return len(containers)

    def calculate_recursive_containers(self):
        # Slow but easy to code solution:
        # We repeat process until there are changes
        # For each container, we add to the list of containers the containers of the container
        changed = False
        iters = 1
        while True:
            print(f'Iter: {iters}')
            changed = False
            for inner, containers in self.c.items():
                for container in containers:
                    if container in self.c:
                        for new_container in self.c[container]:
                            if new_container not in self.c[inner]:
                                changed = True
                                self.c[inner].append(new_container)
            iters += 1
            if not changed:
                break


if __name__ == '__main__':
    with open('day7.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        # Part 1
        c = ContainedIn()
        for line in lines:
            container, contents = parse(line)
            c.add_container_contained(container, contents)
            print(container)
            print(contents)

        print('--------')
        c.calculate_recursive_containers()
        print(c.get_containers('shiny gold'))
        print(len(c.get_containers('shiny gold')))

