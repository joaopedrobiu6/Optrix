import numpy as np

class OpticalObject:
    """ Base class for optical objects

    Parameters
    ----------
    name : str
        Name of the optical object
    """

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name})"

    def __str__(self):
        return f"{self.__class__.__name__}({self.name})"
    
    def __add__(self,  obj1, obj2):
        return 

class ThinLens(OpticalObject):
    """ Thin Lens object

    Parameters
    ----------
    focal_length : float
        Focal length of the thin lens
    """

    def __init__(self, focal_length):
        self.focal_length = focal_length
        self.MELA_ThinLens = np.array([[1, 0], [-1 / focal_length, 1]])

class Mirror(OpticalObject):
    """ Mirror object

    Parameters
    ----------
    radius : float
        Radius of curvature of the mirror. Default is None, which means the mirror is flat.
    """

    def __init__(self, radius=None):
        if radius is not None:
            self.radius = radius
            self.MELA_Mirror = np.array([[1, 0], [2 / self.radius, 1]])
        else:
            self.MELA_Mirror = np.array([[1, 0], [0, 1]])

class FreeSpace(OpticalObject):
    """ Free space propagation object

    Parameters
    ----------
    length : float
        Length of the free space propagation
    """

    def __init__(self, length):
        self.length = length
        self.MELA_FreeSpace = np.array([[1, length], [0, 1]])

class Boundary(OpticalObject):
    """ Boundary object

    Parameters
    ----------
    n1 : float
        Refractive index of the first medium
    n2 : float
        Refractive index of the second medium
    radius : float
        Radius of curvature of the boundary. Default is None, which means the boundary is flat.
    """

    def __init__(self, n1, n2, radius=None):
        self.n1 = n1
        self.n2 = n2
        if radius is not None:
            self.radius = radius
            self.MELA_Boundary = np.array([[1, 0], [- (self.n2 - self.n1) / (self.n2 * self.radius), self.n1 / self.n2]])
        else:
            self.MELA_Boundary = np.array([[1, 0], [0, self.n1 / self.n2]])
            
