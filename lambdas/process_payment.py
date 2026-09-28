import random


def handler(event, context):
    """
    Simula a integração com um serviço de pagamento.
    Regra de simulação: paymentMethod == 'cartao_recusado' força uma recusa,
    qualquer outro método tem 90% de chance de aprovação.
    """
    order = event.get("order", event)
    payment_method = order.get("paymentMethod", "")

    if payment_method == "cartao_recusado":
        approved = False
    else:
        approved = random.random() < 0.9

    return {
        "order": order,
        "paymentApproved": approved,
        "paymentMethod": payment_method,
        "transactionId": f"txn-{order.get('orderId', 'unknown')}",
    }
