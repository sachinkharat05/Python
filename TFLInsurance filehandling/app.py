# import json


# def find_policy(policy_number):

#     with open("policies.json", "r") as file:
#         policies = json.load(file)

#     for policy in policies:

#         if policy["policy_number"] == policy_number:
#             return policy

#     return None


# policy = find_policy("POL1001")

# print(policy)

import json

with open("policies.json", "r") as file:
    policies = json.load(file)

new_policy = {
    "policy_number": "POL1003",
    "customer_name": "Amit",
    "premium": 18000,
    "status": "Active"
}

policies.append(new_policy)

with open("policies.json", "w") as file:
    json.dump(policies, file, indent=4)