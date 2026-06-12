# Fahad Faliz Coder

Autonomous, self-healing full-stack project generator that bypasses token limits by orchestrating targeted file generation.

## Features
- Multi-LLM support (OpenAI, Anthropic, Gemini, Ollama)
- Blueprint-driven DAG generation order
- Symbol tracking for consistency
- Self-healing validation with linters/compilers
- Incremental builds with resume support

## Installation

1. Clone the repository:
```bash
git clone https://github.com/gamesiteonline/Fahad-faliz-coder.git
cd Fahad-faliz-coder
```

2. Install dependencies:
```bash
pip install -e .
# Or manually:
pip install litellm pydantic typer networkx python-dotenv
```

3. (Optional) Install development dependencies:
```bash
pip install -e .[dev]
```

## Setup

Create a `.env` file in the root:
```env
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
GEMINI_API_KEY=...
# For local Ollama, run `ollama serve`
```

## Usage

```bash
# Generate a project
faliz generate blueprint.json --workspace ./my-project --model gpt-4o

# Or with Claude
faliz generate blueprint.json --model claude-3-5-sonnet-20240620

# Local model
faliz generate blueprint.json --model ollama/llama3
```

## Blueprint Example
See `examples/blueprint.json` for a complete Next.js + FastAPI example.

## Project Structure
```
faliz_coder/
├── blueprint.py
├── orchestrator.py
├── providers.py
├── workspace.py
├── validator.py
└── cli.py
```

Built with ❤️ for massive code generation.