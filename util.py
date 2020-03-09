class RuleError(Exception):
    """Exception raised for actions or calls to methods that violate the game
    rules of Magic: the Gathering or that reference an impossible task within
    the framework of the game rules and its definitions.
    """
    pass
