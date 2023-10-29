import requests, json

url = "http://127.0.0.1:8000"
stop = True


def display(data):
    print(json.dumps(data, indent=2))


while stop:
    print(
        "Select what you want to do : \n 1 : get_artists_by_name \n 2 : get_albums_by_name \n 3 : get_tracks_by_album \n 4 : quit"
    )
    match int(input("Your choice : ")):
        case 1:
            display((requests.get(f"{url}/artists/{input('artist name : ')}")).json())
        case 2:
            display((requests.get(f"{url}/albums/{input('album id : ')}")).json())
        case 3:
            display((requests.get(f"{url}/tracks/{input('album id : ')}")).json())
        case 4:
            stop = False
        case _:
            print("You need to choose a number between 1 and 4")
