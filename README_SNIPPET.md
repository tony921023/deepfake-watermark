## 後端最小可執行範例（Flask）

### 安裝 & 執行
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
# source .venv/bin/activate

pip install -r requirements.txt
python app.py
```

### 健康檢查
GET http://127.0.0.1:5000/health

### 範例請求
curl -X POST http://127.0.0.1:5000/api/embed -F "file=@tests/assets/sample.png"

> 目前端點為 stub，可先驗通 API 流程；之後把真實的嵌入/偵測/還原邏輯接進 app.py。
