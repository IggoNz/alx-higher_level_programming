#!/usr/bin/python3
"""Defines an object attribute look up function."""

def lookup(obj):
    """Return the list of an object's available attributes."""
    return (dir(obj))
