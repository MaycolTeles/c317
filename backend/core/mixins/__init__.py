"""
__init__ module to export the classes below.
"""

from .models import DefaultModel
from .serializers import DefaultSerializer


__all__ = [
    "DefaultModel",
    "DefaultSerializer",
]
