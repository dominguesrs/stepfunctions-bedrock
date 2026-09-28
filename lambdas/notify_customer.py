import os
import boto3

TOPIC_ARN = os.environ.get("NOTIFICATIONS_TOPIC_ARN")
sns = boto3.client("sns")


def handler(event, context):
    order = event.get("order", event)
    message = event.get("personalizedMessage", "Seu pedido foi confirmado!")

    sns.publish(
        TopicArn=TOPIC_ARN,
        Subject=f"Pedido {order.get('orderId')} confirmado",
        Message=message,
    )

    return {
        "orderId": order.get("orderId"),
        "status": "notificado",
        "personalizedMessage": message,
    }
