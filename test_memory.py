from memory.memory import store_interaction, search_memory

# Save a test interaction
store_interaction("Hi Echo", "Hello, love. It's always a joy to hear from you.")

# Search memory with a related query
results = search_memory("greeting")

print("\n🔍 Similar Past Messages:\n")
for doc in results:
    print("-", doc)
