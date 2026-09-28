import json
import os
import boto3

MODEL_ID = os.environ.get("BEDROCK_MODEL_ID", "us.anthropic.claude-haiku-4-5-20251001-v1:0")
bedrock = boto3.client("bedrock-runtime")


def build_prompt(order):
    items = ", ".join(order.get("items", []))
    return (
        f"Escreva uma mensagem curta, calorosa e personalizada para {order.get('customerName')} "
        f"confirmando o pedido de delivery contendo: {items}. "
        f"Inclua uma estimativa de tempo de entrega amigável e um tom acolhedor. "
        f"Responda em português, em no máximo 3 frases."
    )


def handler(event, context):
    order = event.get("order", event)
    prompt = build_prompt(order)

    try:
        response = bedrock.converse(
            modelId=MODEL_ID,
            messages=[
                {
                    "role": "user",
                    "content": [{"text": prompt}],
                }
            ],
            inferenceConfig={
                "maxTokens": 200,
                "temperature": 0.7,
                "topP": 0.9,
            },
        )

        message = response["output"]["message"]["content"][0]["text"].strip()

    except Exception as exc:  # noqa: BLE001
        message = (
            f"Olá {order.get('customerName', 'cliente')}, seu pedido foi confirmado "
            f"e já está sendo preparado!"
        )
        print(f"Falha ao chamar o Bedrock, usando mensagem padrão: {exc}")

    return {
        "order": order,
        "personalizedMessage": message,
    }
