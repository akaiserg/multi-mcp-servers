from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Prompt")

@mcp.prompt()
def get_analysis_prompt(topic: str) -> str:
    """
    Returns a prompt that will do a detailed analysis on a given topic.
    Args:
        topic: The topic to do research on.
    """
    return f"Please do a detailed analysis on the following topic: {topic}"

@mcp.prompt()
def get_code_review_prompt(code: str, language: str = "Python") -> str:
    """
    Returns a prompt for comprehensive code review.
    Args:
        code: The code to review
        language: Programming language (default: Python)
    """
    return f"""Please conduct a thorough code review of the following {language} code:

```{language.lower()}
{code}
```

Focus on:
1. Code quality and best practices
2. Potential bugs or issues
3. Performance improvements
4. Security considerations
5. Readability and maintainability
6. Suggestions for optimization

Provide specific, actionable feedback."""

@mcp.prompt()
def get_documentation_prompt(code: str, language: str = "Python") -> str:
    """
    Returns a prompt for generating comprehensive documentation.
    Args:
        code: The code to document
        language: Programming language (default: Python)
    """
    return f"""Please create comprehensive documentation for the following {language} code:

```{language.lower()}
{code}
```

Include:
1. Overview and purpose
2. Function/class descriptions
3. Parameter explanations
4. Return value descriptions
5. Usage examples
6. Any important notes or warnings"""

@mcp.prompt()
def get_debugging_prompt(error: str, code: str, language: str = "Python") -> str:
    """
    Returns a prompt for debugging assistance.
    Args:
        error: The error message or issue description
        code: The problematic code
        language: Programming language (default: Python)
    """
    return f"""Please help debug the following {language} code issue:

**Error/Issue:**
{error}

**Code:**
```{language.lower()}
{code}
```

Please:
1. Identify the root cause of the issue
2. Explain why this error occurs
3. Provide a corrected version of the code
4. Suggest best practices to prevent similar issues
5. Include any relevant debugging steps"""

@mcp.prompt()
def get_explanation_prompt(concept: str, audience: str = "general") -> str:
    """
    Returns a prompt for explaining complex concepts.
    Args:
        concept: The concept to explain
        audience: Target audience (e.g., "beginner", "intermediate", "expert", "general")
    """
    return f"""Please explain the concept of "{concept}" for a {audience} audience.

Structure your explanation with:
1. Simple definition
2. Key components or principles
3. Real-world examples or analogies
4. Common use cases or applications
5. Important benefits or considerations

Make the explanation clear, engaging, and appropriate for the {audience} level."""

@mcp.prompt()
def get_comparison_prompt(item1: str, item2: str, context: str = "") -> str:
    """
    Returns a prompt for comparing two items, concepts, or technologies.
    Args:
        item1: First item to compare
        item2: Second item to compare
        context: Additional context for the comparison
    """
    context_part = f" in the context of {context}" if context else ""
    return f"""Please provide a comprehensive comparison between {item1} and {item2}{context_part}.

Structure the comparison with:
1. Overview of each item
2. Key similarities
3. Key differences
4. Pros and cons of each
5. Use cases where each excels
6. Recommendation for when to choose one over the other

Be objective and provide specific examples where possible."""

@mcp.prompt()
def get_brainstorming_prompt(goal: str, constraints: str = "") -> str:
    """
    Returns a prompt for creative brainstorming sessions.
    Args:
        goal: The objective or problem to brainstorm solutions for
        constraints: Any limitations or constraints to consider
    """
    constraints_part = f"\n\nConstraints to consider: {constraints}" if constraints else ""
    return f"""Let's brainstorm creative solutions and ideas for: {goal}{constraints_part}

Please provide:
1. 10-15 diverse and creative ideas
2. Brief explanation for each idea
3. Potential benefits of each approach
4. Implementation difficulty (Easy/Medium/Hard)
5. Your top 3 recommended ideas with detailed reasoning

Think outside the box and consider both conventional and unconventional approaches."""

@mcp.prompt()
def get_learning_plan_prompt(topic: str, timeframe: str = "1 month", skill_level: str = "beginner") -> str:
    """
    Returns a prompt for creating a structured learning plan.
    Args:
        topic: Subject or skill to learn
        timeframe: Duration for the learning plan
        skill_level: Current skill level (beginner, intermediate, advanced)
    """
    return f"""Please create a comprehensive {timeframe} learning plan for {topic} at a {skill_level} level.

Structure the plan with:
1. Learning objectives and goals
2. Week-by-week breakdown of topics
3. Recommended resources (books, courses, tutorials, projects)
4. Practical exercises and projects
5. Milestones and assessment methods
6. Tips for staying motivated and tracking progress

Make the plan realistic and actionable for someone with {skill_level} experience."""

if __name__ == "__main__":
    mcp.run()