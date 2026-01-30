#!/usr/bin/env python3
"""
OSINT Username Search Tool
Executa Maigret e Sherlock para investigação de usernames
"""

import sys
import json
import subprocess
import os
from datetime import datetime

def run_maigret(username):
    """Executa Maigret e retorna resultados"""
    print(f"🔍 Executando Maigret para: {username}")
    try:
        result = subprocess.run(
            ['maigret', username, '--json', 'simple', '--timeout', '10'],
            capture_output=True,
            text=True,
            timeout=300
        )
        return {
            'success': result.returncode == 0,
            'output': result.stdout,
            'error': result.stderr
        }
    except Exception as e:
        return {
            'success': False,
            'output': '',
            'error': str(e)
        }

def run_sherlock(username):
    """Executa Sherlock e retorna resultados"""
    print(f"🔍 Executando Sherlock para: {username}")
    try:
        result = subprocess.run(
            ['sherlock', username, '--timeout', '10', '--print-found'],
            capture_output=True,
            text=True,
            timeout=300
        )
        return {
            'success': result.returncode == 0,
            'output': result.stdout,
            'error': result.stderr
        }
    except Exception as e:
        return {
            'success': False,
            'output': '',
            'error': str(e)
        }

def parse_results(maigret_result, sherlock_result):
    """Parse e organiza os resultados"""
    findings = []
    
    # Parse Maigret
    if maigret_result['success'] and maigret_result['output']:
        lines = maigret_result['output'].split('\n')
        for line in lines:
            if line.strip() and not line.startswith('['):
                findings.append({
                    'source': 'Maigret',
                    'data': line.strip()
                })
    
    # Parse Sherlock
    if sherlock_result['success'] and sherlock_result['output']:
        lines = sherlock_result['output'].split('\n')
        for line in lines:
            if 'http' in line.lower():
                findings.append({
                    'source': 'Sherlock',
                    'data': line.strip()
                })
    
    return findings

def generate_html_report(username, findings, maigret_result, sherlock_result):
    """Gera relatório HTML"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
    
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Relatório OSINT - {username}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }}
        .container {{
            max-width: 900px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        .header h1 {{
            font-size: 2em;
            margin-bottom: 10px;
        }}
        .username {{
            font-size: 1.5em;
            font-weight: bold;
            background: rgba(255,255,255,0.2);
            padding: 10px 20px;
            border-radius: 10px;
            display: inline-block;
            margin-top: 10px;
        }}
        .content {{
            padding: 30px;
        }}
        .info-box {{
            background: #f8f9fa;
            border-left: 4px solid #667eea;
            padding: 15px;
            margin-bottom: 20px;
            border-radius: 5px;
        }}
        .section {{
            margin-bottom: 30px;
        }}
        .section-title {{
            font-size: 1.5em;
            color: #667eea;
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 2px solid #667eea;
        }}
        .finding {{
            background: #f8f9fa;
            padding: 15px;
            margin-bottom: 10px;
            border-radius: 8px;
            border-left: 4px solid #28a745;
        }}
        .finding a {{
            color: #667eea;
            text-decoration: none;
            word-break: break-all;
        }}
        .finding a:hover {{
            text-decoration: underline;
        }}
        .source-badge {{
            display: inline-block;
            background: #667eea;
            color: white;
            padding: 4px 10px;
            border-radius: 12px;
            font-size: 0.85em;
            margin-right: 10px;
        }}
        .raw-output {{
            background: #2d3748;
            color: #e2e8f0;
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
            line-height: 1.6;
        }}
        .footer {{
            text-align: center;
            padding: 20px;
            color: #666;
            font-size: 0.9em;
        }}
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin-bottom: 30px;
        }}
        .stat-card {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }}
        .stat-number {{
            font-size: 2.5em;
            font-weight: bold;
        }}
        .stat-label {{
            font-size: 0.9em;
            opacity: 0.9;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🔍 Relatório OSINT</h1>
            <div class="username">@{username}</div>
            <p style="margin-top: 15px; opacity: 0.9;">Gerado em: {timestamp}</p>
        </div>
        
        <div class="content">
            <div class="stats">
                <div class="stat-card">
                    <div class="stat-number">{len(findings)}</div>
                    <div class="stat-label">Resultados Encontrados</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">2</div>
                    <div class="stat-label">Ferramentas Utilizadas</div>
                </div>
            </div>
            
            <div class="info-box">
                <strong>ℹ️ Sobre esta investigação:</strong><br>
                Esta busca foi realizada utilizando as ferramentas Maigret e Sherlock para identificar 
                perfis públicos associados ao username fornecido em diversas plataformas online.
            </div>
"""
    
    if findings:
        html += """
            <div class="section">
                <h2 class="section-title">📊 Resultados Consolidados</h2>
"""
        for finding in findings:
            source_color = '#667eea' if finding['source'] == 'Maigret' else '#764ba2'
            html += f"""
                <div class="finding">
                    <span class="source-badge" style="background: {source_color};">{finding['source']}</span>
                    <div style="margin-top: 8px;">{finding['data']}</div>
                </div>
"""
        html += """
            </div>
"""
    
    # Maigret raw output
    if maigret_result['output']:
        html += f"""
            <div class="section">
                <h2 class="section-title">🔍 Maigret - Output Completo</h2>
                <div class="raw-output">{maigret_result['output'].replace('<', '&lt;').replace('>', '&gt;')}</div>
            </div>
"""
    
    # Sherlock raw output
    if sherlock_result['output']:
        html += f"""
            <div class="section">
                <h2 class="section-title">🕵️ Sherlock - Output Completo</h2>
                <div class="raw-output">{sherlock_result['output'].replace('<', '&lt;').replace('>', '&gt;')}</div>
            </div>
"""
    
    # Erros se houver
    errors = []
    if not maigret_result['success'] and maigret_result['error']:
        errors.append(f"Maigret: {maigret_result['error']}")
    if not sherlock_result['success'] and sherlock_result['error']:
        errors.append(f"Sherlock: {sherlock_result['error']}")
    
    if errors:
        html += """
            <div class="section">
                <h2 class="section-title">⚠️ Avisos e Erros</h2>
"""
        for error in errors:
            html += f"""
                <div class="info-box" style="border-left-color: #dc3545;">
                    {error.replace('<', '&lt;').replace('>', '&gt;')}
                </div>
"""
        html += """
            </div>
"""
    
    html += """
        </div>
        
        <div class="footer">
            <p>🛡️ Ferramenta OSINT - GitHub Pages + GitHub Actions</p>
            <p>Relatório gerado automaticamente</p>
        </div>
    </div>
</body>
</html>
"""
    return html

def main():
    if len(sys.argv) < 2:
        print("❌ Uso: python osint_search.py <username>")
        sys.exit(1)
    
    username = sys.argv[1]
    print(f"🚀 Iniciando investigação OSINT para: {username}")
    print("=" * 60)
    
    # Executa as ferramentas
    maigret_result = run_maigret(username)
    sherlock_result = run_sherlock(username)
    
    # Parse resultados
    findings = parse_results(maigret_result, sherlock_result)
    
    # Gera relatório HTML
    html_report = generate_html_report(username, findings, maigret_result, sherlock_result)
    
    # Salva resultados
    output_dir = 'results'
    os.makedirs(output_dir, exist_ok=True)
    
    # Salva HTML
    html_path = f'{output_dir}/{username}_report.html'
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_report)
    print(f"✅ Relatório HTML salvo: {html_path}")
    
    # Salva JSON
    json_data = {
        'username': username,
        'timestamp': datetime.now().isoformat(),
        'findings': findings,
        'maigret': maigret_result,
        'sherlock': sherlock_result
    }
    json_path = f'{output_dir}/{username}_data.json'
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=2, ensure_ascii=False)
    print(f"✅ Dados JSON salvos: {json_path}")
    
    print("=" * 60)
    print(f"✨ Investigação concluída! Total de resultados: {len(findings)}")

if __name__ == '__main__':
    main()
