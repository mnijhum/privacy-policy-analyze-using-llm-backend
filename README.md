# Privacy Policy Analysis using LLM

This is a simple Flask application to chat with Llama3.2 model locally to analyze a website's privacy policy. I am sending a URL from frontend to this server and asking to analyze the website's policy and give feedback with ratings so that we do not have to read the overwhelming essay of privacy policies. 

## Requirements
- Download Ollama from https://ollama.com/
- Python 3.x
- Flask

## Setup
0. **Pull Llama3 model**
   ```bash
   ollama pull llama3.2:latest # You can choose any other model if you want`
   ```
1. **Clone the repository**:

   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Create a virtual environment (optional but recommended)**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

   If you don't have a `requirements.txt` file, you can install Flask directly:

   ```bash
   pip install Flask
   ```

## Running the Application

0. **Start the Flask app**:

   ```bash
   python3 app.py
   ```

1. **Access the application**:

   There is only one endpoint implemented to chat with the LLM. Use `http://127.0.0.1:5000/analyze` from any of your frontend app. Update this code as you want:

   ```python
   @app.route('/analyze', methods=['POST'])
    def analyze():
        data = request.json
        policy_url = data['policyText']
        result = send_url_to_llama(policy_url)
        return jsonify({"analysis": result})
    ```


2. **Model Modification**
   
   If you want to use different model and change the prompt, open this repo in VS Code and go to `model/analyzeWithLlama.py` and edit as you want. In the payload give the model name accurately. 

## Notes

- If you need to specify a different host or port, you can modify `app.run()` in `app.py`:

   ```python
   if __name__ == "__main__":
       app.run(host="0.0.0.0", port=5000)
   ```


