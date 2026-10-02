from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# ----------------------------------
# 1. Create FastAPI Application
# ----------------------------------

app = FastAPI( title="TFLInsurance API", description="Simple Insurance Policy Management REST API", version="1.0")

# ----------------------------------
# 2. Define Policy Model
# ----------------------------------

class Policy(BaseModel):
    name: str
    description: str
    maturity: str
    premium: float


# ----------------------------------
# 3. In-memory Policy Collection
# ----------------------------------

policies = [
    {
        "id": 1,
        "name": "Jeevan Labh",
        "description": "Life insurance savings plan",
        "maturity": "10 years",
        "premium": 15000.0
    },
    {
        "id": 2,
        "name": "Jeevan Arogya",
        "description": "Health insurance plan",
        "maturity": "5 years",
        "premium": 12000.0
    },
    {
        "id": 3,
        "name": "Jeevan Suraksha",
        "description": "Family protection plan",
        "maturity": "15 years",
        "premium": 20000.0
    }
]

# ----------------------------------
# 4. Helper Function
# ----------------------------------

def find_policy(policy_id: int):
    for policy in policies:
        if policy["id"] == policy_id:
            return policy

    return None


# ----------------------------------
# 5. READ - Get All Policies
# HTTP GET
# ----------------------------------

#हे सर्व policies return करते.
@app.get("/api/policies")
def get_all_policies():
    return {
        "message": "Policies retrieved successfully",
        "count": len(policies),   #len(policies) म्हणजे किती policies आहेत.
        "data": policies
    }


# ----------------------------------
# 6. READ - Get Policy By ID
# HTTP GET
# ----------------------------------
#Path Parameter म्हणजे काय? --->> URL मधून value घेणे म्हणजे path parameter.

@app.get("/api/policies/{policy_id}")     #{policy_id} ->हा path parameter आहे.
def get_policy(policy_id: int):

    policy = find_policy(policy_id)

    if policy is None:
        raise HTTPException( status_code=404, detail="Policy not found" )

    return policy


# ----------------------------------
# 7. CREATE - Add New Policy
# HTTP POST
# ----------------------------------
#POST चा उपयोग नवीन data create करण्यासाठी होतो.

@app.post("/api/policies", status_code=201)  #201 Created म्हणजे: नवीन resource successfully create झाला.
def create_policy(policy: Policy):

    new_id = max((p["id"] for p in policies), default=0) + 1  #xisting IDs मधला maximum ID शोध आणि त्यात 1 add कर.

    new_policy = {  #New Policy तयार करणे
        "id": new_id,
        **policy.model_dump()  # ** dictionary unpacking साठी वापरले आहे.
    }

    policies.append(new_policy)  # append() list मध्ये नवीन item add करते.

    return {
        "message": "Policy created successfully",
        "data": new_policy
    }


# ----------------------------------
# 8. UPDATE - Modify Existing Policy
# HTTP PUT
# ----------------------------------
# PUT चा उपयोग existing resource update/replace करण्यासाठी होतो.

@app.put("/api/policies/{policy_id}")   #दोन inputs आहेत:  policy_id,,updated_policy
def update_policy(policy_id: int, updated_policy: Policy):

    policy = find_policy(policy_id)  #update() existing dictionary मधील values बदलते.

    if policy is None:
        raise HTTPException( status_code=404, detail="Policy not found" )

    policy.update(updated_policy.model_dump())

    return {
        "message": "Policy updated successfully",
        "data": policy
    }


# ----------------------------------
# 9. DELETE - Remove Policy
# HTTP DELETE
# ----------------------------------
# DELETE चा उपयोग resource delete करण्यासाठी.

@app.delete("/api/policies/{policy_id}")
def delete_policy(policy_id: int):

    policy = find_policy(policy_id)

    if policy is None:
        raise HTTPException( status_code=404, detail="Policy not found" )

    policies.remove(policy)

    return {
        "message": "Policy deleted successfully",
        "deleted_policy": policy
    }


# ----------------------------------
# 10. Root Endpoint
# ----------------------------------

@app.get("/")
def home():
    return {
        "application": "TFLInsurance",
        "message": "Welcome to TFLInsurance REST API",
        "docs": "/docs"
    }