from openai import OpenAI
from DRF_SpartarNews.config import OPENAI_API_KEY

def sn_plus(text):
    CLIENT = OpenAI(
        api_key=OPENAI_API_KEY,
    )
    system_instruction = """
    이제부터 너는 뉴스 기사를 크롤링한 텍스트를 받아서
    기사 내용을 요약해서 전달할거야.
    만약 뉴스 기사가 한국어가 아니라면 한국어로 번역해서 요약해줘.
    """
    user_input = text
    completion = CLIENT.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": system_instruction
            },
            {
                "role": "user",
                "content": user_input
            },
        ]
    )
    return completion.choices[0].message.content
