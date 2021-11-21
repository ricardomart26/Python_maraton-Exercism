def get_coordinate(record):
    """

    :param record: tuple - a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    return record[1]

def convert_coordinate(coordinate):
    """

    :param coordinate: str - a string map coordinate
    :return:  tuple - the string coordinate seperated into its individual components.
    """
    return (coordinate[0], coordinate[1])


def compare_records(azara_record, rui_record):
    """

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: bool - True if coordinates match, False otherwise.
    """
    address = convert_coordinate(azara_record[1])
    return all(x == address[index] for index, x in enumerate(rui_record[1]))


def create_record(azara_record, rui_record):
    """

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return:  tuple - combined record, or "not a match" if the records are incompatible.
    """

    pass


def clean_up(combined_record_group):
    """

    :param combined_record_group: tuple of tuples - everything from both participants.
    :return: string of tuples separated by newlines - everything "cleaned". Excess coordinates and information removed.
    """
    str = ""
    res = ()
    for elem in combined_record_group:
        if isinstance(elem, tuple):
            for x, i in enumerate(elem):
                print(i)
                if x == 1: continue
                str += ''.join(i)
                if i != elem[-1]:
                    str += ' '
            str += '\n'
    s = str.split('\n')
    for i in s:
        i += '\n'
        print(i)
        res += (i,)
    return res


"""(\"Scrimshaw Whale's Tooth\", 'Deserted Docks', ('2', 'A'), 'Blue')\n\
('Brass Spyglass', 'Abandoned Lighthouse', ('4', 'B'), 'Blue')\n\
('Robot Parrot', 'Seaside Cottages', ('1', 'C'), 'Blue')\n\
('Glass Starfish', 'Tangled Seaweed Patch', ('6', 'D'), 'Orange')\n\
('Vintage Pirate Hat', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange')\n\
('Pirate Flag', 'Windswept Hilltop (Island of Mystery)', ('7', 'F'), 'Orange')\n\
('Crystal Crab', 'Old Schooner', ('6', 'A'), 'Purple')\n\
('Model Ship in Large Bottle', 'Harbor Managers Office', ('8', 'A'), 'Purple')\n\
('Angry Monkey Figurine', 'Stormy Breakwater', ('5', 'B'), 'Purple')\n\
('Carved Wooden Elephant', 'Foggy Seacave', ('8', 'C'), 'Purple')\n\
('Amethyst  Octopus', 'Aqua Lagoon (Island of Mystery)', ('1', 'F'), 'Yellow')\n\
('Antique Glass Fishnet Float', 'Spiky Rocks', ('3', 'D'), 'Yellow')\n\
('Silver Seahorse', 'Hidden Spring (Island of Mystery)', ('4', 'E'), 'Yellow')\n"""

# print(compare_records(("Scrimshaw Whale's Tooth", '2A'), ('Deserted Docks', ('2', 'A'), 'Blue')))
print(clean_up((
            ("Scrimshaw Whale's Tooth", '2A', 'Deserted Docks', ('2', 'A'), 'Blue'),
            ('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue'),
            ('Robot Parrot', '1C', 'Seaside Cottages', ('1', 'C'), 'Blue'),
            ('Glass Starfish', '6D', 'Tangled Seaweed Patch', ('6', 'D'), 'Orange'),
            ('Vintage Pirate Hat', '7E', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange'),
            ('Pirate Flag', '7F', 'Windswept Hilltop (Island of Mystery)', ('7', 'F'), 'Orange'),
            ('Crystal Crab', '6A', 'Old Schooner', ('6', 'A'), 'Purple'),
            ('Model Ship in Large Bottle', '8A', 'Harbor Managers Office', ('8', 'A'), 'Purple'),
            ('Angry Monkey Figurine', '5B', 'Stormy Breakwater', ('5', 'B'), 'Purple'),
            ('Carved Wooden Elephant', '8C', 'Foggy Seacave', ('8', 'C'), 'Purple'),
            ('Amethyst  Octopus', '1F', 'Aqua Lagoon (Island of Mystery)', ('1', 'F'), 'Yellow'),
            ('Antique Glass Fishnet Float', '3D', 'Spiky Rocks', ('3', 'D'), 'Yellow'),
            ('Silver Seahorse', '4E', 'Hidden Spring (Island of Mystery)', ('4', 'E'), 'Yellow')
        )))
