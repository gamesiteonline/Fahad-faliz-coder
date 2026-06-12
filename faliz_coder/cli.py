import typer
from pathlib import Path
from .orchestrator import CognitiveOrchestrator
from .blueprint import load_blueprint

app = typer.Typer()

@app.command()
def generate(blueprint_path: Path, workspace: Path = Path("./generated-project"), model: str = "gpt-4o"):
    blueprint = load_blueprint(blueprint_path)
    orchestrator = CognitiveOrchestrator(workspace=workspace, default_model=model)
    orchestrator.generate_project(blueprint)
    print("✅ Generation complete!")

if __name__ == "__main__":
    app()