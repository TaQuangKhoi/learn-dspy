"""
RAG (Retrieval-Augmented Generation) Example
=============================================
This example demonstrates how to build a simple RAG system with DSPy.
"""

import os
import dspy


def main():
    """Run a RAG example."""
    print("=" * 50)
    print("RAG System Example with DSPy")
    print("=" * 50)
    
    print("\n1. Setting up the model...")
    
    # Check if API key is available
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("   ⚠️  OPENAI_API_KEY not found in environment")
        print("   Please set it to run this example:")
        print("   export OPENAI_API_KEY='your-api-key'")
        return
    
    # Configure DSPy with OpenAI
    lm = dspy.LM(model='openai/gpt-4o-mini', api_key=api_key)
    dspy.configure(lm=lm)
    print("   ✓ Model configured: gpt-4o-mini")
    
    print("\n2. Defining RAG signature...")
    
    class GenerateAnswer(dspy.Signature):
        """Answer questions based on retrieved context."""
        context = dspy.InputField(desc="Retrieved relevant documents")
        question = dspy.InputField()
        answer = dspy.OutputField(desc="Answer derived from context")
    
    print("   ✓ Signature defined")
    
    print("\n3. Creating RAG module...")
    
    class SimpleRAG(dspy.Module):
        def __init__(self):
            super().__init__()
            self.generate_answer = dspy.ChainOfThought(GenerateAnswer)
        
        def forward(self, question, documents):
            # Combine documents into context
            context = "\n\n".join(documents)
            # Generate answer
            prediction = self.generate_answer(context=context, question=question)
            return prediction
    
    rag = SimpleRAG()
    print("   ✓ RAG module created")
    
    print("\n4. Preparing sample documents...")
    
    documents = [
        "DSPy is a framework that helps you optimize LM prompts and weights algorithmically.",
        "DSPy provides composable modules for instructing language models using Python syntax.",
        "The framework automatically optimizes prompts through compilation and evaluation.",
        "DSPy allows you to build complex LM pipelines with modules like ChainOfThought and ReAct.",
    ]
    
    print(f"   ✓ Loaded {len(documents)} documents")
    
    print("\n5. Running example queries...")
    
    questions = [
        "What is DSPy?",
        "How does DSPy help with prompts?",
        "What modules does DSPy provide?",
    ]
    
    for i, question in enumerate(questions, 1):
        print(f"\n   Question {i}: {question}")
        try:
            response = rag(question=question, documents=documents)
            print(f"   Answer: {response.answer}")
            if hasattr(response, 'rationale'):
                print(f"   Reasoning: {response.rationale}")
        except Exception as e:
            print(f"   Error: {str(e)}")
    
    print("\n" + "=" * 50)
    print("RAG Example completed!")
    print("=" * 50)
    print("\nNote: In a real RAG system, you would:")
    print("- Use a vector database for document retrieval")
    print("- Implement semantic search")
    print("- Add document chunking and embedding")
    print("=" * 50)


if __name__ == "__main__":
    main()
