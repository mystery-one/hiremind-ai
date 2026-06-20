from mcp.server import register_tool, call_tool

from tools.embedding_tool import generate_embedding
from tools.scoring_tool import calculate_final_score

# Register tools
register_tool("embedding_tool", generate_embedding)
register_tool("scoring_tool", calculate_final_score)

# Example usage
embedding = call_tool(
    "embedding_tool",
    "Python machine learning engineer"
)

score = call_tool(
    "scoring_tool",
    90,
    85,
    80
)

print("Embedding Generated")
print("Final Score:", score)