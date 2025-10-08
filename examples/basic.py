"""
Basic DSPy Example
==================
This example demonstrates the basic usage of DSPy with a simple signature.
"""

import dspy


def main():
    """Run a basic DSPy example."""
    print("=" * 50)
    print("Basic DSPy Example")
    print("=" * 50)
    
    # Configure DSPy with a local model or OpenAI
    # For this example, we'll show how to set up the model
    print("\n1. Setting up DSPy model...")
    print("   Note: You need to configure an LLM in your environment.")
    print("   Options:")
    print("   - OpenAI: Set OPENAI_API_KEY environment variable")
    print("   - Local models: Use Ollama or other local LLM servers")
    
    # Example: Configure with OpenAI (commented out to avoid errors)
    # lm = dspy.LM(model='openai/gpt-4o-mini', api_key=os.getenv('OPENAI_API_KEY'))
    # dspy.configure(lm=lm)
    
    print("\n2. Define a simple signature...")
    
    # Define a simple signature
    class BasicQA(dspy.Signature):
        """Answer questions with short factoid answers."""
        question = dspy.InputField()
        answer = dspy.OutputField(desc="often between 1 and 5 words")
    
    print("   Signature: BasicQA")
    print("   Input: question")
    print("   Output: answer (1-5 words)")
    
    print("\n3. Create a predictor...")
    # Create a predictor using the signature
    qa = dspy.Predict(BasicQA)
    print("   Predictor created: dspy.Predict(BasicQA)")
    
    print("\n4. Example usage (requires configured LLM):")
    print("   response = qa(question='What is the capital of France?')")
    print("   print(response.answer)  # Expected: 'Paris'")
    
    print("\n" + "=" * 50)
    print("To run this with a real LLM:")
    print("1. Set up your API key (e.g., OPENAI_API_KEY)")
    print("2. Uncomment the configuration code above")
    print("3. Run: uv run python examples/basic.py")
    print("=" * 50)


if __name__ == "__main__":
    main()
