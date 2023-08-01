# Infrared-ChatBot
<img src="/static/images/demo2.png">


- I have developed a state-of-the-art chatbot using large language models (LLM), integrating OpenAI APIs and Langchain. The primary purpose of this chatbot is to efficiently fetch datasets from URLs and enable seamless communication with other users.
- In the initial phase, I conducted extensive experiments in a research environment, utilizing the power of Google Colab. Subsequently, I refined the code by transforming it into a modular structure, and then seamlessly transferred the model to a development environment. Here, I skillfully designed an interactive web application, harnessing my expertise in web development.
- To streamline the deployment process, I expertly employed Docker and GitHub Actions, creating effective CI/CD pipelines. For the final deployment, I harnessed the capabilities of AWS EC2 and ECR instances, ensuring a robust and scalable solution for the chatbot's deployment.

## Steps to Run it
### 1. Cloning the Repository
```bash
git clone https://github.com/MANMEET75/Infrared-OpenAIChatBot.git
```
### 2. Creating the virtual environment using anaconda
```bash
conda create -p venv python=3.10 -y
```

### 3. Activate the virtual environment
```bash
conda activate venv/
```

### 4. Installing the dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the following commands in your anaconda prompt one by one
#### First Command
```bash
conda install -c pytorch faiss-cpu
```

#### Second Command
```bash
conda install -c conda-forge faiss
```

## 6. Check the InfraBot
```bash
python app.py
```

# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.ap-south-1.amazonaws.com/mlproj

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app

Enjoy Coding!
