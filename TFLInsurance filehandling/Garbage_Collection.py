import sys

policy = { 
    "policy_id": "POL1001",
    "customer": "Ravi",
    "coverage": 1000000
}

print(sys.getrefcount(policy))