import redis


def test_redis_connection():
    client = redis.Redis(
        host="localhost",
        port=6379,
        decode_responses=True,
    )

    client.set("ci_test_key", "Hello Redis")

    value = client.get("ci_test_key")

    assert value == "Hello Redis"

    client.delete("ci_test_key")
