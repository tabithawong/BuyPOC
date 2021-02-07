import gspread
from oauth2client.service_account import ServiceAccountCredentials

client_secret = {
  "type": "service_account",
  "project_id": "uottahack-304005",
  "private_key_id": "10d8b2a616458d9c8125c274523c81769327bc66",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCcXSOcgW9APP85\nAPQk0m2YDyLIyLgvaohC/Qq+ld6Gj+wmpdVZfYQNT+iWBzJNANeVkZVogeR1UU02\nSonAAagoi78mJVjQRLia4U2whik/Ftsmc9nplHWiPfHNJQdSgVb+pA3pTIH8kvgV\nLj1mLh/VTzgpYwR6fTfJ34hf5edXQAANk5IQlFlJ9Z3g0KF0IG/5MZ0MEC5x67hg\nDrr1T084m9KrGaLLjKKm0goMjnNj2VqWpGJRwjuSXsOzRYweUjbRbmk3u5S5FNU6\n12f/Fy73z4HAVuI7Px9VAMF1j03d8LnQbSfb+/VjEsVGg6b67lJvBn6nC9/gyGbs\nQlo6ucJBAgMBAAECggEAOEDT0nbIaOJo6X+b1fF0Zxuu5nA7vydC7WKurmEphNyb\nV04a4s6ips1kPjFJmeVfKdqN12K/p6s/rXQEebS+5BNeieEuwgKvLV03/3VMuntF\nDWDpeTylU2CYsLaNG1QX0ZWAwbl6HD1djfUsNqoKXsnYyR7r2gtZekF2hRWndD4s\nr23+dDyjGKBhDhXB/LEstYpqJYY0NqP8RCqCkb/tan4uVPGSd5RDxO+XDUIf6yoM\nufm49K6NrISREVJ5WMioiINISKwrkK/NegjZzoydm8b8zDvbLt8H+wn2ZL6mIaWJ\nOUyCgjOE1wzjRtWvEbJGmR7S25dRlNgKmR1ufVHCpwKBgQDKLcQ287MfBzMtJ5DH\nQcgv5H/i8FbJhyJ9Ec+a62BuUpWCh1qi9E0LjhMRWBrnrAJ9VY36mlGPdh2rLtWQ\n6e51ZbrEg8pKrMHQk3wwEahKcOhhh7fOTG9moIYv+Atag/iyD7pxIf3GuU5r8/R1\nLSiuHRY/kA5QJEFAK9Tn/bivLwKBgQDF/SPx50/SVRfctz4lmWklaWZtET9/Fg1h\nuAwpVfAU+TQ0mlYMe6vOZK/hGKJqwZAVWdEVjnqb2Dd1YqiIRwFdM4aCeWGmEdNA\np9+6mMwh5X66Ko2t2yrUu9G8TOYtVvyQmHIXFllgZusc+O22e2rQJ3gPxFgm18IL\ndXhmkDzJjwKBgQClgHFuym+Gps4t2IWbly3YhqRpkXR55DVHTJ01pBh8Nv5Mq6B2\nZKXtH5BcUlMz8orXLoHa8xhw56/BwcTxq42YbH5G/9tI5cKCizjN4KZyyZpwvDiq\nl8dZq24tNk+U+RNML7PfiIPFeUvI8xraEO2MGiNsRPByijsf3MGcZwYX4QKBgCPv\nYTHL0RIU/cLCw5XhdVMkAUI0ijjP0Nf2psZt4ah83rvZc1rKq5FHdyC87uW/gh5N\n8gQemyRkJxS4NmydrqKy8mwGCfIxdA1dKt9cUliopcq2ZIa0q952xIeP0YtTKX45\nHSQRm2FC7NOSXtrrJaToNQNvmKxcJs0boiHDdjUDAoGAbB32R/KuqSRC1oM5TtZp\ntxn/AoUH04MBwqboZF51iFuzzcSxTHF3lMfmWrpzYL97QFE0mnYj3WmlkoIECbsg\nGft9yw8wgWViOcuNmOhbg7cUCiQDSUuTnY/TV/AjX+mUtOVnaBUYg5f3V3tcczjJ\nee0unHS7r0hvb30iZuUZOfY=\n-----END PRIVATE KEY-----\n",
  "client_email": "uottahackttm@uottahack-304005.iam.gserviceaccount.com",
  "client_id": "109417915691044543368",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/uottahackttm%40uottahack-304005.iam.gserviceaccount.com"
}

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_dict(client_secret, scope)
client = gspread.authorize(creds)
sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1_1T6Hbj809Y5sqPMqYxrkFnxACwWpz0720Plo68h5Bk/edit#gid=0").sheet1


def get_whole():
  return sheet.get_all_values()


def get_store(id_):
  return sheet.get_all_values()[id_]


def add_store(name, site, category, address, country):
  sheet.append_row([name, site, category, address, None, country])