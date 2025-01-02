# LLMs in Love

_LLMs in Love_ is a conversational AI project that simulates interactions between two distinct AI-personas, Ethan and Sally. The project leverages the LangChain framework and OpenRouter's language models to create engaging and dynamic dialogues.


## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/rajtilakjee/llmsinlove.git
    cd llmsinlove
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your OpenRouter API key:
    ```
    OPENROUTER_API_KEY=your_openrouter_api_key
    ```

## Usage

To start the conversation simulation, run the `main.py` script:

```sh
python app/main.py
```

You can adjust the number of turns in the conversation by modifying the `num_turns` variable in `main.py`.