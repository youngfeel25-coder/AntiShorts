import os
import io
import datetime
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv import load_dotenv

# .env 로드
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

# 구글 드라이브 읽기 전용 및 문서 읽기 권한
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
# 프로젝트의 다운로드 기본 디렉터리
KNOWLEDGE_BASE_DIR = os.path.join(os.path.dirname(__file__), '..', 'knowledge_base')

def authenticate():
    creds = None
    token_path = os.path.join(os.path.dirname(__file__), '..', 'token.json')
    credentials_path = os.path.join(os.path.dirname(__file__), '..', 'credentials.json')

    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
        
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(credentials_path):
                print("❌ 오류: 'credentials.json' 파일이 없습니다.")
                print("1. 구글 클라우드 콘솔(https://console.cloud.google.com)로 이동")
                print("2. 새 프로젝트 생성 후 'Google Drive API' 사용 설정")
                print("3. 사용자 인증 정보(OAuth 2.0 클라이언트 ID - 데스크톱 앱) 생성")
                print("4. JSON 다운로드 후 이름을 'credentials.json'으로 변경하여 d:\\Anti 폴더에 넣으세요.")
                return None
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)
            
        with open(token_path, 'w') as token:
            token.write(creds.to_json())
            
    return creds

def sync_docs(creds):
    try:
        service = build('drive', 'v3', credentials=creds)

        # NotebookLM에서 내보낸 기본 파일 형식 (Google Docs) 중 최근 10개 조회
        print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] 구글 드라이브 스캔 중... (MimeType: Google Docs)")
        results = service.files().list(
            q="mimeType='application/vnd.google-apps.document'",
            pageSize=10, fields="nextPageToken, files(id, name, modifiedTime)",
            orderBy="modifiedTime desc"
        ).execute()
        
        items = results.get('files', [])

        if not items:
            print("최근 업데이트된 Google 문서를 찾을 수 없습니다.")
            return

        os.makedirs(KNOWLEDGE_BASE_DIR, exist_ok=True)
        
        print(f"발견된 문서: {len(items)}개. 동기화 시작합니다.")
        for item in items:
            file_name = item['name'].replace('/', '_') + ".txt"
            file_path = os.path.join(KNOWLEDGE_BASE_DIR, file_name)
            
            # 파일이 이미 존재하면 건너뛰기 (여기서는 단순 덮어쓰기/수정시간 비교 생략)
            print(f"➡️ '{item['name']}' 다운로드 중...")
            try:
                # 텍스트 파일로 내보내기(Export)
                request = service.files().export_media(fileId=item['id'], mimeType='text/plain')
                response = request.execute()
                
                with open(file_path, 'wb') as f:
                    f.write(response)
                    
            except HttpError as e:
                print(f"파일 다운로드 실패 ({item['name']}): {e}")
                
        print(f"✅ 동기화 완료! 파일은 '{KNOWLEDGE_BASE_DIR}'에 저장되었습니다.")

    except HttpError as error:
        print(f"An error occurred: {error}")

def main():
    print("=======================================")
    print("🤖 코부장 연동 시스템: 구글 문서(NotebookLM 내보내기) 자동 수집기")
    print("=======================================")
    creds = authenticate()
    if creds:
        sync_docs(creds)

if __name__ == '__main__':
    main()
