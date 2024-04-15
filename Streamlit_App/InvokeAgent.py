from boto3.session import Session
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
from botocore.credentials import Credentials
import json
import os
from requests import request
import boto3
import base64
import io
import sys

#For this to run on a local machine in VScode, you need to set the AWS_PROFILE environment variable to the name of the profile/credentials you want to use. 


#check for credentials
#echo $AWS_ACCESS_KEY_ID
#echo $AWS_SECRET_ACCESS_KEY
#echo $AWS_SESSION_TOKEN


def call_bedrock_knowledge_base(prompt, region, model_id, kb_id):
    
    bedrock_agent_client = boto3.client("bedrock-agent-runtime", region_name="us-east-1")

    model_arn = f'arn:aws:bedrock:{region}::foundation-model/{model_id}'
    
    # You can create a prompt template to specificy your output. Do that here and uncomment the section in the bedrock call below to use it. 
    # prompt_template = "You are a technician assistant. You will be asked questions about turbine maintenance. Please reference the knowledge base and provide the answers to the question."
    
    results = bedrock_agent_client.retrieve_and_generate(
        input={'text': prompt},
        retrieveAndGenerateConfiguration={
            'type': 'KNOWLEDGE_BASE',
            'knowledgeBaseConfiguration': {
                'knowledgeBaseId': kb_id,
                'modelArn': model_arn,
                # 'generationConfiguration': {
                #     'promptTemplate': {
                #         'textPromptTemplate': prompt_template
                #     }
                # }
            }
        }
    )
    text_response = results["citations"][0]["generatedResponsePart"]["textResponsePart"]["text"]
    citation = ""
    if results["citations"][0]:
        if results["citations"][0]["retrievedReferences"]:
            citation = "\n \n I got that info from here: " + results["citations"][0]["retrievedReferences"][0]["location"]["s3Location"]["uri"]

    if citation == "":
        citation = " No citation available."
    return_list = [text_response, citation]
    return return_list
    