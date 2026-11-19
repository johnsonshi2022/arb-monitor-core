import asyncio
import time

async def exponential_backoff_reconnect(max_retries=5):
    for i in range(max_retries):
        try:
            # Simulate connection attempt
            print(f"[{time.strftime('%H:%M:%S')}] Trying to connect... attempt {i+1}")
            await asyncio.sleep(0.5)
            print("Connected successfully")
            return True
        except Exception as e:
            wait = 2 ** i
            print(f"Connection failed: {e}, retry in {wait}s")
            await asyncio.sleep(wait)
    return False

async def single_leg_stop_loss(leg_filled: bool, other_leg_filled: bool, timeout=3):
    """
    Handle one-leg fill risk in cross-exchange arbitrage.
    If only one leg is filled, force close after timeout.
    """
    if leg_filled and not other_leg_filled:
        print("One leg filled, waiting for hedge...")
        await asyncio.sleep(timeout)
        if not other_leg_filled:
            print("Timeout reached, forcing market close on single leg")
            return "STOP_LOSS_TRIGGERED"
    return "OK"

# Example usage
# asyncio.run(exponential_backoff_reconnect())
