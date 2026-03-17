# Day 3 - Simple AI Assistant

def greet_user(name):
    return f"Hello {name}, welcome back to your AI journey!"

def suggest_topic():
    topics = [
        "Learn Python functions",
        "Explore APIs",
        "Understand LLM basics",
        "Build a simple automation script"
    ]
    
    print("\nHere are your suggested topics for today:")
    
    for topic in topics:
        print("-", topic)

def main():
    print("=== AI Assistant Day 3 ===")
    
    name = input("Enter your name: ")
    
    greeting = greet_user(name)
    print(greeting)
    
    suggest_topic()
    
    print("\nKeep going. You're building momentum 🚀")

if __name__ == "__main__":
    main()