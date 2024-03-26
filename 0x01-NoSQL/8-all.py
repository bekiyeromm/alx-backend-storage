#!/usr/bin/env python3
"""
Python function that lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    function to list all the documents in the collection
    args:
        mongo_collection: pymongo collection object
    Return: list of documents in the collection on success
    or an empty list if no document in the collection
    """
    return [list_of_doc for list_of_doc in mongo_collection.find()]
