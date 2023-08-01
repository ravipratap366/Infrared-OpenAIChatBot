# Infrared-ChatBot
<img src="/static/images/demo2.png">


- I have developed a state-of-the-art chatbot using large language models (LLM), integrating OpenAI APIs and Langchain. The primary purpose of this chatbot is to efficiently fetch datasets from URLs and enable seamless communication with other users.
- In the initial phase, I conducted extensive experiments in a research environment, utilizing the power of Google Colab. Subsequently, I refined the code by transforming it into a modular structure, and then seamlessly transferred the model to a development environment. Here, I skillfully designed an interactive web application, harnessing my expertise in web development.
- To streamline the deployment process, I expertly employed Docker and GitHub Actions, creating effective CI/CD pipelines. For the final deployment, I harnessed the capabilities of AWS EC2 and ECR instances, ensuring a robust and scalable solution for the chatbot's deployment.

## Steps to Run it
### Cloning the Repository
```bash
git clone https://github.com/MANMEET75/Infrared-ChatBot.git
```
### Creating the virtual environment using anaconda
```bash
conda create -p venv python=3.10 -y
```

### Activate the virtual environment
```bash
conda activate venv/
```

### Installing the dependencies
```bash
pip install -r requirements.txt
```

### Run the following commands in your anaconda prompt one by one
#### First Command
```bash
conda install -c pytorch faiss-cpu
```

#### Second Command
```bash
conda install -c conda-forge faiss
```

## Check the InfraBot
```bash
python app.py
```


Enjoy Coding!
