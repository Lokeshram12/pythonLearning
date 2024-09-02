import requests

def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response=requests.get(url)
    data=response.json()

    if data["success"] and "data" in data:
        user_data=data["data"]
        username=user_data["login"]["username"]
        return username
    else:
        raise Exception("failed to fetch the user data")

def main():
    try:
        username=fetch_random_user()
        print(username)
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()