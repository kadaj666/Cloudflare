from celery import shared_task



@shared_task(queue="default", default_retry_delay=30, max_retries=3)
def sync_accounts():
    pass
    return ("cloudflare synced")


