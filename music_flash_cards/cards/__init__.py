"""Flash Card Resource Files 

Resources are anything that isn't code but required
by the program to function.
"""

from typing import List

from importlib.resources import contents, is_resource, path


def note_card_paths() -> List[str]:
    """
    Returns a list of strings representing filesystem paths
    to PNG images of musical notes.

    :return: List[str]
    """

    pkg = "music_flash_cards.cards.chromatic_note_cards"

    note_cards = []

    for note_card_name in contents(pkg):
        if is_resource(pkg, note_card_name) and note_card_name.endswith(".png"):
            with path(pkg, note_card_name) as note_card_path:
                note_cards.append(str(note_card_path))
    return note_cards


def incorrect_card_path() -> str:
    """Returns a string path to the incorrect card."""

    with path("music_flash_cards.cards", "Incorrect.png") as card_path:
        return str(card_path)


def correct_card_path() -> str:
    """Returns a string path to the correct card."""

    with path("music_flash_cards.cards", "Correct.png") as card_path:
        return str(card_path)
