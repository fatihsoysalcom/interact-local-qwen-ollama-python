# Interact Local Qwen Ollama Python

This Python script demonstrates how to interact with a locally running Large Language Model (LLM) like Qwen, using the Ollama Python client library. It sends a predefined prompt to the specified Qwen model hosted by Ollama and prints the model's response. The example assumes Ollama is installed and the target model is pulled.

## Language

`python`

## How to Run

1. Ensure Ollama is installed and running (run `ollama serve` in a terminal).
2. Pull the Qwen model: `ollama pull qwen:7b` (or your preferred Qwen tag).
3. Install the Python client: `pip install ollama`.
4. Run the script: `python ollama_qwen_interaction.py`.

## Original Article

This example accompanies the Turkish article: [Qwen 3 ve VS Code ile Ücretsiz Yapay Zeka Geliştirme: Ollama ile Tam Kurulum Rehberi](https://fatihsoysal.com/blog/qwen-3-ve-vs-code-ile-ucretsiz-yapay-zeka-gelistirme-ollama-ile-tam-kurulum-rehberi/).

## License

MIT — see [LICENSE](LICENSE).
