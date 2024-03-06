import xml.etree.ElementTree as ET
import os
import re
from bs4 import BeautifulSoup

# Path to the Stack Exchange data dump XML file
data_dump_path = '/path/to/stack_exchange_data_dump/stackoverflow.com-Posts.xml'

# Output directory to save the preprocessed data
output_dir = '/path/to/output/directory'

# Regular expression pattern to remove HTML tags
html_tag_pattern = re.compile(r'<.*?>')

# Function to preprocess text
def preprocess_text(text):
    # Remove HTML tags
    text = re.sub(html_tag_pattern, '', text)
    # Remove extra whitespaces
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

# Function to extract questions and answers from the data dump
def extract_questions_answers(data_dump_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    question_file = open(os.path.join(output_dir, 'questions.txt'), 'w', encoding='utf-8')
    answer_file = open(os.path.join(output_dir, 'answers.txt'), 'w', encoding='utf-8')

    with open(data_dump_path, 'r', encoding='utf-8') as f:
        for event, elem in ET.iterparse(f):
            if elem.tag == 'row':
                post_type_id = elem.get('PostTypeId')
                if post_type_id == '1':  # Question
                    question_id = elem.get('Id')
                    title = elem.get('Title')
                    body = elem.get('Body')
                    body = BeautifulSoup(body, 'html.parser').get_text()  # Remove HTML tags
                    title = preprocess_text(title)
                    body = preprocess_text(body)
                    question_file.write(f"{question_id}\t{title}\t{body}\n")
                elif post_type_id == '2':  # Answer
                    answer_id = elem.get('Id')
                    question_id = elem.get('ParentId')
                    body = elem.get('Body')
                    body = BeautifulSoup(body, 'html.parser').get_text()  # Remove HTML tags
                    body = preprocess_text(body)
                    answer_file.write(f"{answer_id}\t{question_id}\t{body}\n")
                elem.clear()

    question_file.close()
    answer_file.close()

# Extract questions and answers from the data dump
extract_questions_answers(data_dump_path, output_dir)
