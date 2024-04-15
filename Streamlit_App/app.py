import InvokeAgent as agenthelper
import streamlit as st
import json
import pandas as pd
from PIL import Image, ImageOps, ImageDraw

# Specify the model, region, and knowledge base ID, and title
model_id = "anthropic.claude-3-haiku-20240307-v1:0" # This is the model ID. You can find this in Bedrock under the model you want to use.
region = "us-east-1" 
kb_id = "SFZ4L3HHIS" # This is the knowledge base ID
knowledge_base_title = "Octank Internal Asset Assitant" # This is the title of the knowledge base. Rename it based on the kind of application you are building.

# Streamlit page configuration
st.set_page_config(page_title="AI Powered Assistant", page_icon=":robot_face:", layout="wide")

# Function to crop image into a circle
def crop_to_circle(image):
    mask = Image.new('L', image.size, 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.ellipse((0, 0) + image.size, fill=255)
    result = ImageOps.fit(image, mask.size, centering=(0.5, 0.5))
    result.putalpha(mask)
    return result

# Title
st.title("Custom Generative AI Assistant")

# Display a text box for input
prompt = st.text_input("Please enter your query?", max_chars=2000)
prompt = prompt.strip()

# Display a primary button for submission
submit_button = st.button("Submit", type="primary")

# Display a button to end the session
end_session_button = st.button("End Session")

# Sidebar for user input
infomation = "This is a generative AI application that can answer questions about using RAG running on an Amazon Bedrock Knowledge Base. Please ask a question and click submit."
st.sidebar.text_area(knowledge_base_title,value=infomation, height=300)
    

# Session State Management
if 'history' not in st.session_state:
    st.session_state['history'] = []

# Function to parse and format response
def format_response(response_body):
    try:
        # Try to load the response as JSON
        data = json.loads(response_body)
        # If it's a list, convert it to a DataFrame for better visualization
        if isinstance(data, list):
            return pd.DataFrame(data)
        else:
            return response_body
    except json.JSONDecodeError:
        # If response is not JSON, return as is
        return response_body



# Handling user input and responses
if submit_button and prompt:
    event = {
        "sessionId": "MYSESSION",
        "question": prompt
    }
    response = agenthelper.call_bedrock_knowledge_base(prompt, region, model_id, kb_id)
    
    
    # Use the following line to format the response as JSON
    responseFormatted = response[0] + response[1]
    st.session_state['history'].append({"question": prompt, "answer": responseFormatted})

    

    
    
    

if end_session_button:
    st.session_state['history'].append({"question": "Session Ended", "answer": "Thank you for using AnyCompany Support Agent!"})
    event = {
        "sessionId": "MYSESSION",
        "question": "placeholder to end session",
        "endSession": True
    }
    agenthelper.lambda_handler(event, None)
    st.session_state['history'].clear()


# Display conversation history
st.write("## Conversation")

for chat in reversed(st.session_state['history']):
    
    # Creating columns for Question
    col1_q, col2_q = st.columns([0.3, 3.5])
    with col1_q:
        human_image = Image.open('images/human_face.png')
        circular_human_image = crop_to_circle(human_image)
        st.image(circular_human_image, width=125)
    with col2_q:
        st.text_area("Q:", value=chat["question"], height=50, key=str(chat)+"q", disabled=True)

    # Creating columns for Answer
    col1_a, col2_a = st.columns([0.3, 3.4])
    if isinstance(chat["answer"], pd.DataFrame):
        with col1_a:
            robot_image = Image.open('images/robot_face.jpg')
            circular_robot_image = crop_to_circle(robot_image)
            st.image(circular_robot_image, width=100)
        with col2_a:
            st.dataframe(chat["answer"])
    else:
        with col1_a:
            robot_image = Image.open('images/robot_face.jpg')
            circular_robot_image = crop_to_circle(robot_image)
            st.image(circular_robot_image, width=150)
        with col2_a:
            st.text_area("A:", value=chat["answer"], height=175, key=str(chat)+"a")

