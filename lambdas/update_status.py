import os
import time
import boto3

TABLE_NAME = os.environ.get("ORDERS_TABLE_NAME", "DeliveryOrders")
dynamodb = boto3.resource("dynamodb")


def handler(event, context):
    order = event.get("order", event)
    status = event.get("status", "recebido")

    table = dynamodb.Table(TABLE_NAME)
    table.put_item(
        Item={
            "orderId": str(order.get("orderId")),
            "customerName": order.get("customerName", ""),
            "items": order.get("items", []),
            "address": order.get("address", ""),
            "status": status,
            "personalizedMessage": event.get("personalizedMessage", ""),
            "updatedAt": int(time.time()),
        }
    )

    return {
        "order": order,
        "status": status,
        "personalizedMessage": event.get("personalizedMessage", ""),
    }
