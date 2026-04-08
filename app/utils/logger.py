import time
import logging

logging.basicConfig(level=logging.INFO)

def log_request(query: str):
    return {
        "query": query,
        "start_time": time.time()
    }

def log_response(log_data, response: str):
    log_data["response"] = response
    log_data["end_time"] = time.time()
    log_data["latency"] = log_data["end_time"] - log_data["start_time"]

    logging.info(log_data)
    return log_data
def log_llm_usage(response):
    try:
        usage = response.response_metadata.get("token_usage", {})
        return {
            "prompt_tokens": usage.get("prompt_tokens"),
            "completion_tokens": usage.get("completion_tokens")
        }
    except:
        return {}
