# Recyclable and Low Fat Products
#     - This is a typical SQL query problem that requires filtering products based on their attributes.

# Problem:
# You are given a table named Products with the following schema:

# Table: Products
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | product_id  | int     |
# | product_name | varchar |
# | recyclable  | enum('Yes', 'No') |
# | low_fat     | enum('Yes', 'No') |
# +-------------+---------+
# product_id is the primary key.
# recyclable is either "Yes" or "No".
# low_fat is either "Yes" or "No".


# Q - Write an SQL query to retrieve all product_id and product_name of products that are both recyclable and low fat.

# SQL Solution:

# SELECT product_id, product_name
# FROM Products
# WHERE recyclable = 'Yes' AND low_fat = 'Yes';

# Time Complexity: O(N) (Scans the table once)
# Space Complexity: O(1) (No extra storage is used)
