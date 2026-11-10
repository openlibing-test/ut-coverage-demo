# ut-coverage-demo

用于验证 `openlibing-test/upload-ut-action@v1.0.2` 在 GitHub Actions 下的 UT 覆盖率上报链路。

## 内容

- `calculator.py` / `test_calculator.py`：pytest 用例覆盖的示例模块
- `.github/workflows/ut-coverage.yml`：运行 `coverage run -m pytest` 生成 `coverage.json`，再通过 `upload-ut-action` 上报

## 预期链路

1. 平台识别为 GitHub Actions，OBS 桶使用 `openlibing-github-action`
2. OIDC 换证（`GitHubActions` 提供商 + `github-actions` 委托）
3. 解析 `coverage.json` → 上传 OBS → 回调 `POST /action-api/ut/coverage/report`

## 本地运行

```bash
pip install -r requirements.txt
coverage run -m pytest -q
coverage json
```
