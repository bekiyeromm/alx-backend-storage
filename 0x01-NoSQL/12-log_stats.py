#!/usr/bin/env python3

"""
Python script that provides some stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient

""" Connect to MongoDB"""
client = MongoClient('localhost', 27017)
db = client.logs
collection = db.nginx

"""Count total number of logs"""
total_logs = collection.count_documents({})

print(f"{total_logs} logs")

"""Count number of logs for each method"""
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = {method: collection.count_documents(
    {"method": method}) for method in methods}

print("Methods:")
for method in methods:
    print(f"\tmethod {method}: {method_counts[method]}")

"""Count number of logs with method=GET and path=/status"""
status_logs_count = collection.count_documents(
    {"method": "GET", "path": "/status"})
print(f"{status_logs_count} status check")
