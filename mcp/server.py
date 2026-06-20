TOOLS = {}

def register_tool(tool_name, tool_function):

    TOOLS[tool_name] = tool_function

def call_tool(tool_name, *args):

    if tool_name not in TOOLS:
        raise ValueError(f"Tool {tool_name} not found")

    return TOOLS[tool_name](*args)