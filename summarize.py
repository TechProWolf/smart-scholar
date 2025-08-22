from flask import Blueprint, request, jsonify
from utils.summarizer import summarize_text

summarize_bp = Blueprint('summarize', __name__)

@summarize_bp.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    text = data.get('text', '')
    length = data.get('length', 'medium')
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    summary = summarize_text(text, length)
    return jsonify({'summary': summary})
