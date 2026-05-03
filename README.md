# Quenade

AI-powered local coding assistant for code review, security analysis, and repository scanning.

## Features

- **Code explanation**  
  Understand what every line of code does.

- **Code review**  
  Receive suggestions to improve readability, maintainability, and code quality.

- **Security analysis**  
  Detect potential vulnerabilities and insecure coding practices.

- **Repository scanning**  
  Analyze single files or entire repositories.

- **100% local execution**  
  Powered by Ollama. Your code never leaves your machine.

- **Prompt-based architecture**  
  Specialized prompts for explanation, review, and security analysis.

## Stack

- **Language:** Python
- **LLM Engine:** Ollama
- **Model:** Qwen2
- **OS:** Linux

## Project Structure

```text
quenade/
├── main.py
├── agent/
│   ├── core.py
│   └── prompts.py
├── utils/
│   ├── file_reader.py
│   └── repository_reader.py
```

## Installation

Install Ollama:

https://ollama.com

Pull the model:

```bash
ollama pull qwen2:0.5b
```

Clone the project:

```bash
git clone <your-repository>
cd quenade
```

## Usage

### Analyze a single file

```bash
python3 main.py explain file.py
python3 main.py review file.py
python3 main.py security file.py
```

### Analyze an entire repository

```bash
python3 main.py explain .
python3 main.py review .
python3 main.py security .
```

## Example Output

```text
Analyzing: main.py

Security findings:
NO SECURITY ISSUES FOUND

Risk level:
LOW
```

## Future Roadmap

- Static analysis integration
- Risk scoring
- JSON/Markdown reports
- Multi-language support
- Parallel repository scanning

## Author

Máximo Hugo Quiñones