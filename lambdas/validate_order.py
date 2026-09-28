import json


REQUIRED_FIELDS = ["orderId", "customerName", "items", "address", "paymentMethod"]


def handler(event, context):
    """Valida os campos obrigatórios do pedido recebido."""
    missing = [field for field in REQUIRED_FIELDS if not event.get(field)]

    if missing:
        return {
            "isValid": False,
            "reason": f"Campos obrigatórios ausentes: {', '.join(missing)}",
            "order": event,
        }

    if not isinstance(event.get("items"), list) or len(event["items"]) == 0:
        return {
            "isValid": False,
            "reason": "O pedido precisa ter ao menos um item.",
            "order": event,
        }

    return {
        "isValid": True,
        "reason": "Pedido válido.",
        "order": event,
    }
