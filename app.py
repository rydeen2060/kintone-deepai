from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import time

app = Flask(__name__)

# CORS設定 - kintoneからのアクセスを許可
CORS(app, origins=[
    'https://8i4xch433rrn.cybozu.com',
    'https://8i4xch433rrn.kintone.com'
])

# APIキー
API_KEY = 'demo-api-key-2025'

print('=' * 60)
print('DeepAI Demo Server for kintone')
print('=' * 60)

@app.route('/')
def root():
    return jsonify({
        'service': 'DeepAI Server for kintone',
        'version': '1.0.0',
        'status': 'running',
        'message': 'サーバーは正常に動作しています',
        'endpoints': {
            'deepai': 'POST /api/deepai',
            'health': 'GET /health'
        }
    })

@app.route('/health')
def health():
    return jsonify({
        'status': 'ok',
        'timestamp': datetime.now().isoformat(),
        'uptime': f'{int(time.time())} seconds'
    })

@app.route('/api/deepai', methods=['POST'])
def deepai():
    # APIキー認証
    api_key = request.headers.get('X-API-Key', '')
    if api_key != API_KEY:
        print(f'✗ 認証エラー: 無効なAPIキー')
        return jsonify({
            'success': False,
            'error': '認証エラー: 無効なAPIキー'
        }), 401

    try:
        data = request.get_json()
        if not data:
            return jsonify({
                'success': False,
                'error': 'リクエストボディが必要です'
            }), 400

        record_id = data.get('recordId', 'unknown')
        app_id = data.get('appId', 'unknown')
        business_id = data.get('businessId', '')
        account_name = data.get('accountName', '')

        print('\n' + '=' * 60)
        print('✓ リクエスト受信')
        print(f'  Record ID: {record_id}')
        print(f'  App ID: {app_id}')
        print(f'  Business ID: {business_id}')
        print(f'  Account Name: {account_name}')
        print('=' * 60)

        if not business_id and not account_name:
            return jsonify({
                'success': False,
                'error': 'businessId または accountName が必要です'
            }), 400

        current_date = datetime.now().strftime('%Y年%m月%d日')
        current_time = datetime.now().strftime('%H:%M:%S')

        feedback = f"""{account_name} 様

お世話になっております。

【分析結果】
ビジネスID「{business_id}」について、DeepAIによる分析を実施いたしました。

◆ 現状評価
現在の活動状況は良好で、継続的な成長傾向が確認できました。
直近30日間のデータを分析した結果、安定した運用が行われています。

◆ デモ環境情報
- 実行環境: Flask (Python)
- デプロイ方式: Render
- リアルタイム処理: 対応

◆ 今後の推奨事項
・データ収集の継続
・定期的なモニタリングの実施
・異常値検知システムの活用

分析日時: {current_date} {current_time}
レコードID: {record_id}

※これはデモ環境です。本番環境では実際のAI APIと連携します。"""

        summary = f"
