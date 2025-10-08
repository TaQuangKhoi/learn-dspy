"""
Learn DSPy - Main Entry Point
==============================
This is the main entry point for the learn-dspy project.
Run specific examples using: uv run example-<name>
"""


def main():
    print("=" * 60)
    print("Welcome to Learn DSPy!")
    print("=" * 60)
    print("\nDSPy is a framework for algorithmically optimizing LM prompts")
    print("and weights, with composable modules in Pythonic syntax.")
    print("\n" + "=" * 60)
    print("Available Examples:")
    print("=" * 60)
    print("\n1. Basic Example (No API key required)")
    print("   Command: uv run python examples/basic.py")
    print("   Or:      ./run-basic.sh")
    print("   Description: Learn DSPy signatures and predictors")
    
    print("\n2. QA System (Requires API key)")
    print("   Command: uv run python examples/qa_system.py")
    print("   Or:      ./run-qa.sh")
    print("   Description: Build a question-answering system")
    
    print("\n3. RAG Example (Requires API key)")
    print("   Command: uv run python examples/rag_example.py")
    print("   Or:      ./run-rag.sh")
    print("   Description: Build a Retrieval-Augmented Generation system")
    
    print("\n" + "=" * 60)
    print("Quick Start:")
    print("=" * 60)
    print("1. Copy .env.example to .env")
    print("2. Add your OPENAI_API_KEY to .env")
    print("3. Run any example: uv run python examples/basic.py")
    print("\n" + "=" * 60)
    print("For more information, see README.md")
    print("=" * 60)


if __name__ == "__main__":
    main()

