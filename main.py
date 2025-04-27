from agno.agent import Agent
from agno.models.openai import OpenAIChat

# Basic working agent just to verify deployment
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="Simple starter agent",
    markdown=True
)

# Just a hello-world like agent call
if __name__ == "__main__":
    response = agent.run("Say hello to the world!")
    print(response)
