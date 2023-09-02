# -*- coding: utf-8 -*-
"""Implementation of component system."""
import logging

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)


def log_function_call(func):
    """Decorator to log function calls."""
    def wrapper(*args, **kwargs):
        LOGGER.info(f"Calling {func.__name__}...")
        result = func(*args, **kwargs)
        LOGGER.info(f"{func.__name__} returned {result}")
        return result
    return wrapper
