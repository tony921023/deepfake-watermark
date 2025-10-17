# Deepfake 防護、偵測與還原系統

將影像處理 / 模型推論流程 **API 化**：
1) `/api/embed`：嵌入浮水印（容器影像）
2) `/api/detect`：偵測竄改與風險分數
3) `/api/reveal`：提取／還原浮水印（含灰階穩定化、TTA、多尺度等）

## 功能亮點
- 前後端整合：Fetch + FormData 上傳、批次輸出與下載
- 一致的 JSON 格式與錯誤碼（便於前端與測試）
- Postman / curl 測試腳本、簡報與報告（27042/27037 條列）

## 快速開始（範例）
```bash
python -m venv .venv && source .venv/bin/activate  # Windows 請用 .venv\Scripts\activate
pip install -r requirements.txt
python app.py  # 啟動 Flask API
```

## API 範例
```bash
curl -X POST http://127.0.0.1:5000/api/reveal   -F "file=@tests/images/container.png"
```

## Roadmap
- [ ] 加入 Swagger (flask-swagger-ui) 或 ReDoc
- [ ] Dockerfile 與 GitHub Actions 部署
- [ ] 評分/最佳小圖自動挑選策略可視化
```
