from settlement import settle_payment_v9


def pay2(total):
    # Settle in USD via the vendored upstream engine.
    return settle_payment_v9(total, "usd")
