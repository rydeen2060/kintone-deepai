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

        summary = f"""【DeepAI分析レポート - デモ環境】

■ 基本情報
- アカウント: {account_name}
- ビジネスID: {business_id}
- 分析日時: {current_date} {current_time}
- データソース: Flask Demo Server

■ 総合評価
当該アカウントは定期的にアクティブであり、データ品質も高水準を維持しています。
機械学習モデルによる予測では、今後も安定的な成長が期待できます。

■ 主要指標
- アクティビティスコア: 85/100
- データ品質: 良好
- 成長トレンド: 上昇傾向
- リスク評価: 低

■ 推奨アクション
1. 現在の運用方針を継続
2. 月次でのパフォーマンスレビュー実施
3. 新規施策の段階的導入を検討

■ 次回分析予定
次回の詳細分析は30日後を推奨します。
継続的なモニタリングにより、より精度の高い予測が可能になります。

■ 技術情報
- 実行環境: Flask (Python)
- リクエストID: {record_id}
- 処理時刻: {current_date} {current_time}

※本分析はデモ環境での自動生成です。
※本番環境では実際のAI APIと連携して高度な分析を提供します。"""

        return jsonify({
            'success': True,
            'feedback': feedback,
            'summary': summary,
            'timestamp': datetime.now().isoformat(),
            'metadata': {
                'recordId': record_id,
                'appId': app_id,
                'processedAt': datetime.now().isoformat(),
                'environment': 'demo'
            }
        })

    except Exception as e:
        print(f'✗ エラー発生: {str(e)}')
        return jsonify({
            'success': False,
            'error': f'サーバーエラー: {str(e)}'
        }), 500

if __name__ == '__main__':
    print('\nサーバーを起動しています...')
    print('✓ http://localhost:5000 でアクセスできます\n')
    app.run(host='0.0.0.0', port=5000, debug=True)
