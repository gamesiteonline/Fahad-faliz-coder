from pydantic import BaseModel, Field
from typing import List, Dict, Any
from pathlib import Path
import json

class ProjectBlueprint(BaseModel):
    name: str
    frontend: dict
    backend: dict
    database: list = []
    infrastructure: dict = {}

def load_blueprint(path: Path):
    data = json.loads(path.read_text())
    return ProjectBlueprint.model_validate(data)