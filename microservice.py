from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Request models
class NumbersRequest(BaseModel):
    numbers: List[int]


class MilestoneRequest(BaseModel):
    numbers: List[int]
    milestone: float


# Endpoint 1: Calculate Average
@app.post("/api/average")
def calculate_average(request: NumbersRequest):
    numbers = request.numbers
    if not numbers: 
        return {"error": "List of numbers is empty."}
    average = sum(numbers) / len(numbers)
    return {"average": average}


# Endpoint 2: Count Values
@app.post("/api/counts")
def count_values(request: NumbersRequest):
    numbers = request.numbers
    count_0 = numbers.count(0)
    count_100 = numbers.count(100)
    count_1_99 = sum(1 for num in numbers if 1 <= num <= 99)
    return {
        "count_0": count_0,
        "count_100": count_100,
        "count_1_99": count_1_99
    }


# Updated Milestone Difference Endpoint
@app.post("/api/milestone-difference")
def milestone_difference(request: MilestoneRequest):
    numbers = request.numbers
    milestone = request.milestone
    if not numbers:
        return {"error": "List of numbers is empty."}
    
    average = sum(numbers) / len(numbers)

    reached = average >= milestone

    needed_for_milestone = max(0, milestone - average)

    return {
        "reached": reached,
        "current_average": average,
        "needed_for_milestone": needed_for_milestone
    }

