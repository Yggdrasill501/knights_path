# -*- coding: utf-8 -*-
import pytest
from algorythm import KnightsPath

class KnightsPathTest(KnightsPath):
    """Test for KhigtsPath class"""
    def __init__(self, playground: list) -> None:
        """Initialisation and preparation of the tets"""
        super().__init__(playground)
        