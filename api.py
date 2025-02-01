import openai
import re
import whisper

def transcribe_audio(mp3_filename):
    """
    Transcribes speech from an MP3 file using OpenAI Whisper.
    """
    model = whisper.load_model("base")
    result = model.transcribe(mp3_filename)
    return result["text"]

def summarize_conversation(conversation_text):
    """
    Uses OpenAI's GPT API to summarize a conversation and extract tasks assigned/received.
    """
    prompt = f"""
    Summarize the following conversation and extract key points.
    Also, identify all tasks assigned (who assigned, who received, and task description).
    Format the output as:
    
    Summary:
    - [Summary Points]
    
    Tasks Assigned:
    - [Assigner] -> [Receiver]: [Task Description]
    
    Conversation:
    {conversation_text}
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an assistant that extracts summaries and tasks from conversations."},
                  {"role": "user", "content": prompt}]
    )
    
    return response['choices'][0]['message']['content']

def extract_tasks(summary_text):
    """
    Extracts structured task assignments from the summarized text using regex.
    """
    task_pattern = re.compile(r'- (\w+) -> (\w+): (.+)')
    tasks = task_pattern.findall(summary_text)
    
    task_list = []
    for assigner, receiver, task in tasks:
        task_list.append({"assigner": assigner, "receiver": receiver, "task": task})
    
    return task_list

if __name__ == "__main__":
    mp3_file = "voice.mp3"
    conversation = transcribe_audio(mp3_file)
    
    summary = summarize_conversation(conversation)
    print("Summary:")
    print(summary)
    
    tasks = extract_tasks(summary)
    print("\nExtracted Tasks:")
    for task in tasks:
        print(f"{task['assigner']} assigned to {task['receiver']}: {task['task']}")
