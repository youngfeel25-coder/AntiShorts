# Anti-Shorts Home PC One-Click Setup Script
# 관리자 권한으로 실행해주세요.

$workDir = "d:\Anti"
$repoUrl = "https://github.com/youngfeel25-coder/AntiShorts.git"

Write-Host "--- 코부장의 홈 PC 워크플레이스 구축을 시작합니다 ---" -ForegroundColor Cyan

# 1. 폴더 생성
if (!(Test-Path $workDir)) {
    New-Item -ItemType Directory -Path $workDir
    Write-Host "[1/4] 폴더 생성 완료: $workDir"
}

Set-Location $workDir

# 2. 저장소 복제
if (!(Test-Path "$workDir\.git")) {
    Write-Host "[2/4] GitHub에서 제작팀 본부를 불러오는 중..."
    git clone $repoUrl .
} else {
    Write-Host "[2/4] 이미 본부가 설치되어 있습니다. 최신 상태로 업데이트합니다."
    git pull origin main
}

# 3. 파이썬 의존성 설치
Write-Host "[3/4] PD들의 도구를 세팅 중입니다 (requirements.txt)..."
python -m pip install -r requirements.txt

# 4. 마무리 안내
Write-Host ""
Write-Host "--- 구축 완료! ---" -ForegroundColor Green
Write-Host "마지막으로 사무실에서 쓰시던 .env 파일을 $workDir 폴더에 넣어주세요."
Write-Host "이제 집에서도 '코부장'을 부르시면 바로 일이 시작됩니다!"
Write-Host ""
Read-Host "엔터를 누르면 종료됩니다..."
