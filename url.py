import urllib.request
with urllib.request.urlopen("https://storage.googleapis.com/kaggle-datasets/14506/21473/file5.json?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1530081386&Signature=PFSGrVvaZ%2BmAytXxmrKscv8AD06dP3kl%2F4AxSr5%2F5Ej3ACPBFF8QwfEI0AcABzc1gg0DOLczgqX%2FWCGdxZI4Oc1a0AaEiKEdUEMqIycEX2CgWeYYA6Z9u0OgBuQKjS4m722UlzY1%2FaiiWq0JUuntWdhjrUE3y%2BBhEpyf%2B%2FvjoTNdnoKc4VQDpLG8DJJhx%2F%2BKMghwmiLglWEw2UIaBm42rcEfWZq%2F9cp%2FwLrPHyN02YOwU2jm9m9cBGNxIgNCKSuwey9YiNHg8hwTSPYnOLpy6g6gM4He%2Bp87m5YaT0bqsWPbhQoZ%2FLZAK4ugWMOghjWap3NyUHCsCYcz%2FX05N8iciQ%3D%3D") as resp:
    html=resp.read()
print(html)
