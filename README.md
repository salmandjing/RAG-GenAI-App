# AI-Powered Custom Q&A Assistant

This repository showcases the integration of Generative AI, Retrieval-Augmented Generation (RAG), and the Bedrock knowledge base to create an interactive and informative web application using Streamlit.

## Prerequisites

Before getting started, ensure that you have the following prerequisites:

1. **Python Installed**: Make sure you have Python installed on your system.
2. **AWS CLI Installed**: Install the AWS Command Line Interface (CLI) to interact with AWS services.
3. **AWS IAM Identity/Role**: Set up an IAM identity or role with the necessary permissions to access Bedrock and other required AWS services. Set up access in your terminal using  ```aws configure ```. [Learn more here](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)

## Getting Started
1. **Clone the Repository**: Clone this repository to your local machine.
2. **Navigate to the Streamlit Folder**: Change your working directory to the `streamlit` folder within the cloned repository.
3. **Install Dependencies**: Run the following command to install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. **S3 File**: Add a file to an S3 bucket that you want to use as the foundation for your Bedrock knowledge base.
5. **Bedrock Access**: Ensure that you have access to the Bedrock model you want to use in your application.
6. **Knowledge Base Setup**: Set up your Bedrock knowledge base using the S3 file from the previous step. Make a note of your knowledge base ID.

7. **Configure the Application**: Open the `app.py` file and update the following lines with your specific information:
   ```python
   # Specify the model, region, and knowledge base ID, and title
   model_id = "anthropic.claude-3-sonnet-20240229-v1:0"  # This is the model ID. You can find this in Bedrock under the model you want to use.
   region = "us-east-1" # Specify the region you are using
   kb_id = "XXXX"  # This is the knowledge base ID
   knowledge_base_title = "XXXX"  # This is the title of the knowledge base. Rename it based on the kind of application you are building. Ex: Wind Turbine Technician / Travel Agent Advisor
   ```
8. **Run the Application**: Open a terminal, navigate to the `streamlit` folder, and run the following command:
   ```
   streamlit run app.py
   ```
   This will launch the Streamlit application in your default web browser.

## Application Overview

This project demonstrates the power of Generative AI, Retrieval-Augmented Generation (RAG), and the Bedrock knowledge base by creating an interactive web application using Streamlit.

The key features of this application include:

- **Generative AI**: The application leverages a powerful language model, such as Claude 3, to generate human-like text responses.
- **Retrieval-Augmented Generation (RAG)**: The RAG framework combines the language model with a structured knowledge base (Bedrock) to provide more informative and grounded responses.
- **Bedrock Knowledge Base**: The Bedrock knowledge base serves as the foundation for the application, providing a rich source of information that the AI can draw upon.
- **Streamlit Interface**: The Streamlit framework is used to create an intuitive and user-friendly web application, making the AI-powered capabilities accessible to users.

Through this application, you can explore the capabilities of Generative AI, RAG, and Bedrock, and see how they can be integrated to tackle real-world use cases in an engaging and informative way.

## Contributing

If you'd like to contribute to this project, feel free to submit a pull request or raise an issue. We welcome any feedback, suggestions, or improvements that can help enhance the project.

## License

This project is licensed under the [MIT License](LICENSE).
