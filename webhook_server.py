from flask import Flask, request
import subprocess
import os

app = Flask(__name__)

@app.route("/", methods=["POST"])
def handle_webhook():
    data = request.get_json()
    print(f"📦 받은 데이터: {data}")

    # FFmpeg 등 외부 명령 실행 시 경로 문제 방지
    result = subprocess.run(["python", "generate_video.py"], capture_output=True, text=True)
    print(f"🎬 실행 결과: {result.stdout}")

    return "🎯 영상 생성 요청 완료", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render는 포트를 환경 변수로 지정함
    app.run(host="0.0.0.0", port=port)
