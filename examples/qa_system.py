"""
Question-Answering System Example
==================================
This example demonstrates how to build a simple QA system with DSPy.
"""

import os
import dspy


def main():
    """Run a QA system example."""
    print("=" * 50)
    print("QA System Example with DSPy")
    print("=" * 50)
    
    print("\n1. Setting up the model...")
    
    # Check if API key is available
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("   ⚠️  OPENAI_API_KEY not found in environment")
        print("   Please set it to run this example:")
        print("   export OPENAI_API_KEY='your-api-key'")
        print("\n   Alternatively, use a local model with Ollama:")
        print("   lm = dspy.LM('ollama/llama2', api_base='http://localhost:11434')")
        return
    
    # Configure DSPy with OpenAI
    lm = dspy.LM(model='openai/gpt-4o-mini', api_key=api_key)
    dspy.configure(lm=lm)
    print("   ✓ Model configured: gpt-4o-mini")
    
    print("\n2. Defining QA signature...")
    
    class QuestionAnswer(dspy.Signature):
        """Answer questions with detailed, accurate responses."""
        context = dspy.InputField(desc="Background information")
        question = dspy.InputField()
        answer = dspy.OutputField(desc="Detailed answer based on context")
    
    print("   ✓ Signature defined")
    
    print("\n3. Creating predictor...")
    qa_predictor = dspy.ChainOfThought(QuestionAnswer)
    print("   ✓ ChainOfThought predictor created")
    
    print("\n4. Running example questions...")
    
    # Example context
    context = """
    DSPy is a framework for algorithmically optimizing LM prompts and weights.
    It provides composable and declarative modules for instructing LMs in a familiar Pythonic syntax.
    DSPy stands for Declarative Self-improving Language Programs in Python.
    """
    
    questions = [
        "What does DSPy stand for?",
        "What is DSPy used for?",
        "What kind of syntax does DSPy use?",
    ]
    
    for i, question in enumerate(questions, 1):
        print(f"\n   Question {i}: {question}")
        try:
            response = qa_predictor(context=context, question=question)
            print(f"   Answer: {response.answer}")
            if hasattr(response, 'rationale'):
                print(f"   Rationale: {response.rationale}")
        except Exception as e:
            print(f"   Error: {str(e)}")
    
    print("\n" + "=" * 50)
    print("Example completed!")
    print("=" * 50)


if __name__ == "__main__":
    main()
