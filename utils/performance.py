def get_page_load_time(driver):
    """Return page load time in milliseconds using the Navigation Timing API.

    Tries performance.getEntriesByType('navigation') first (modern browsers),
    falls back to window.performance.timing for older implementations.
    Returns -1 on failure.
    """
    try:
        # Prefer Navigation Timing Level 2
        script = (
            "var perf = window.performance || {};\n"
            "if (perf.getEntriesByType) { var nav = perf.getEntriesByType('navigation')[0]; if (nav) return nav.loadEventEnd - nav.startTime; }\n"
            "if (perf.timing) { var t = perf.timing; return t.loadEventEnd - t.navigationStart; }\n"
            "return -1;"
        )
        result = driver.execute_script(script)
        # Ensure we return an int (ms)
        if result is None:
            return -1
        try:
            return int(result)
        except Exception:
            return float(result)
    except Exception:
        return -1

