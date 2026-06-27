from langchain_core.prompts import ChatPromptTemplate



def greet(name):

    prompt = ChatPromptTemplate.from_template(
        "Explain {topic} in one sentence."
    )

    message = prompt.invoke({"topic": "Docker"})

    return f"Hello {name}! Docker's message is {message}"

if __name__ == "__main__":
    print(greet("Students"))