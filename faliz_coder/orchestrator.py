from pathlib import Path
from .blueprint import ProjectBlueprint
from .providers import BaseLLMProvider

class CognitiveOrchestrator:
    def __init__(self, workspace: Path, default_model: str):
        self.workspace = workspace
        self.default_model = default_model
        self.provider = BaseLLMProvider()

    def generate_project(self, blueprint: ProjectBlueprint):
        print(f"Generating project {blueprint.name} in {self.workspace}")
        # Full impl in repo with DAG, self-healing etc.