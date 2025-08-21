

def get_variables():
    """
    Returns a list of variables used in the model.
    """
    raise NotImplementedError("The get_variables method must be implemented in a subclass.")


def get_parameters():
    """
    Returns a list of parameters used in the model.
    """
    raise NotImplementedError("The get_parameters method must be implemented in a subclass.")


def calc_rhs():
    """
    Computes the right-hand side of the model.
    """
    raise NotImplementedError("The calc_rhs method must be implemented in a subclass.")

