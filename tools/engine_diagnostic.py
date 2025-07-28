def engine_diagnostic(temp, vib, oil):
    issues = []
    if temp > 100:
        issues.append("High temperature")
    elif temp <= 100:
        issues.append("Temprature is normal")
    if vib > 0.8:
        issues.append("Abnormal vibration")
    elif vib <= 0.8:
        issues.append("Vibrations are normal")
    if oil < 30:
        issues.append("Low oil pressure")
    elif oil >= 30:
        issues.append("Oil pressure is normal")

    return issues or ["All systems nominal"]
