from flask import Blueprint, request, jsonify
from .db import get_db_connection  # 🔹 Importar a conexão com o banco

# 🔹 Criando o Blueprint antes de usá-lo
routes = Blueprint('routes', __name__)

@routes.route('/api/write', methods=['POST'])
def write_to_db():
    conn = None
    cursor = None
    try:
        data = request.get_json()
        print("📌 Dados recebidos:", data)

        if not data:
            return jsonify({'error': 'No data provided'}), 400

        # Mapeamento dos campos
        pedido = data.get('Pedido')
        codigo = data.get('Codigo')
        nota = data.get('Nota')
        pontos = data.get('Pontos')
        faturamento = data.get('Faturamento')
        nome = data.get('Nome')
        diamante = data.get('Diamante')
        uf = data.get('Uf')
        transportadora = data.get('Transportadora')
        pagamento = data.get('Pagamento')
        valor = data.get('Valor')
        valor_frete = data.get('Valor_Frete')
        juros = data.get('Juros')
        credito = data.get('Credito')
        valor_total = data.get('Valor_Total')
        liberado_por = data.get('Liberado_Por')

        if not pedido:
            return jsonify({'error': 'Missing required field: Pedido'}), 400

        conn = get_db_connection()
        cursor = conn.cursor()

        query = """INSERT INTO dbo.sales (
            Pedido, Codigo, Nota, Pontos, Faturamento, Nome, Diamante, Uf, 
            Transportadora, Pagamento, Valor, Valor_Frete, Juros, Credito, 
            Valor_Total, Liberado_Por
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

        cursor.execute(query, (
            pedido, codigo, nota, pontos, faturamento, nome, diamante, uf, 
            transportadora, pagamento, valor, valor_frete, juros, credito, 
            valor_total, liberado_por
        ))

        conn.commit()

        return jsonify({'message': '✅ Data successfully written to the database'}), 200

    except Exception as e:
        print("❌ Erro:", e)
        return jsonify({'error': str(e)}), 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
