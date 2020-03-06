class Face:
    """
    The face of a specific MTG card. Most Magic cards have a single face, but some cards have multiple faces. A face can have any of these characteristics, but may lack specific characteristics, such as the CMC of the transformed
    """
    def __init__(self):
        self.uid = -1
        self.name = ""      # may match Card.name or be a part of it

class Card:
    """
    An MTG card and all of its characteristics, including multiple faces.
    """
    def __init__(self):
        """
        -1 indicates a numeric value has not been set
        '' indicates a string value has not been set
        """
        self.uid = -1    # a unique id for each card
        self.name = ""  # no default name
        self.ref = {
            "scryfall_id": -1,
            "oracle_id": -1,
            "mtgo_id": -1,
            "arena_id": -1,
            "lang": "en",           # NOTE: English is presumed default
            "scryfall_uri": "",
            "scryfall_api_uri": ""
        }
        self.multiface = False
        self.multiface_type = None  # None, split, transform, adventure, etc.
        self.face = {}  # main, front/back, split-a split-b, etc.
