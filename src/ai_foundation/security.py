def redact_secret(value: str) -> str:
    """Hide a secret before displaying it in logs."""
    if not value:
        return ""
    return "[REDACTED]"
