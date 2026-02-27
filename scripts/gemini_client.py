import os
import sys
import argparse
from google import genai
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

# UTF-8 출력 설정 (Windows 터미널 등에서 이모지/한글 출력 지원)
if sys.stdout.encoding != 'utf-8':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def get_client():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY not found in .env file.")
        print("Please copy .env.example to .env and fill in your API Key.")
        sys.exit(1)
    
    return genai.Client(api_key=api_key)

def generate_content(client, prompt, model_name="gemini-2.0-flash"):
    try:
        response = client.models.generate_content(
            model=model_name,
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    parser = argparse.ArgumentParser(description="Google AI Studio Gemini Client (New SDK)")
    parser.add_argument("prompt", help="The prompt to send to Gemini")
    parser.add_argument("--model", default="gemini-2.0-flash", help="Model name (e.g., gemini-2.0-flash, gemini-1.5-pro)")
    parser.add_argument("--silent", action="store_true", help="Disable completion sound")
    
    args = parser.parse_args()
    
    client = get_client()
    result = generate_content(client, args.prompt, args.model)
    print(result)
    
    # 작업 완료 후 알림음 (Windows 전용)
    if not args.silent:
        try:
            import winsound
            # 띵~ 하는 느낌의 고음 (주파수, 지속시간ms)
            winsound.Beep(1000, 200)
            winsound.Beep(1500, 300)
        except ImportError:
            # 타 OS 고려
            print("\a", end="") # 표준 비프음
            pass

if __name__ == "__main__":
    main()
