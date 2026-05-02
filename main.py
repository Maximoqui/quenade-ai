import sys
import subprocess

from utils.file_reader import read_file
from agent.core import QuenadeAgent


def ollama_llm(prompt: str):

    result = subprocess.run(
        ["ollama", "run", "qwen2:0.5b"],
        input=prompt,
        text=True,
        capture_output=True
    )

    return result.stdout


def main():

    if len(sys.argv) < 3:

        print("Usage: python3 main.py [explain|review] <file>")
        return


    command = sys.argv[1]

    file_path = sys.argv[2]


    code = read_file(file_path)


    agent = QuenadeAgent(ollama_llm)


    if command == "explain":

        result = agent.explain(code)


    elif command == "review":

        result = agent.review(code)
        
    elif command == "security":

        result = agent.security(code)


    else:

        result = "Unknown command"


    print(result)


if __name__ == "__main__":
    main()