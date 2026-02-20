import requests

BASE_URL = "https://jsonmock.hackerrank.com/api/medical_records"


# How to get paginated data, access nested data and filter on requirements.
def getData(doctorName, diagnosisId):
    min_temp = float("inf")
    max_temp = float("-inf")

    page = 1

    while True:
        resp = requests.get(BASE_URL, params={"page": page})
        resp.raise_for_status()
        data = resp.json()

        # process records
        for record in data.get("data", []):
            if (
                record.get("doctor", {}).get("name") == doctorName
                and record.get("diagnosis", {}).get("id") == diagnosisId
            ):
                temp = record.get("vitals", {}).get("bodyTemperature")
                if temp is not None:
                    min_temp = min(min_temp, temp)
                    max_temp = max(max_temp, temp)

        # pagination end check
        if page >= data.get("total_pages", 0):
            break

        page += 1

    # no matching records case
    if min_temp == float("inf"):
        return []

    return [int(min_temp), int(max_temp)]


print(getData("Dr Arnold Bullock", 2))
