import json

FILE_NAME = 'youtube.txt'

def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open(FILE_NAME, 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f" {index}. {video['name']}, Duration:{video['time']}")
    print("\n")
    print("*" * 70)

def add_video(videos):
    name = input("Enter video name : ")
    time = input("Enter furation of video : ")
    videos.append({'name':name, 'time':time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    choice = int(input("Choose the video you want to update :"))
    if 1 <= choice and choice <= len(videos):
        name = input("Enter the new name of video :")
        time = input("Enter the new duration of video :")
        videos[choice-1] = {'name':name, 'time':time}
        save_data_helper(videos)
    else :
        print("Invalid index selected")

def delete_video(videos):
    list_all_videos(videos)
    choice = int(input("Choose the video you want to delete :"))
    if 1 <= choice and choice <= len(videos):
        del videos[choice-1]
        save_data_helper(videos)
    else :
        print("Invalid index selected")

def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager")
        print("1. list all youtube video")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a video")
        print("5. Exit the app")
        choice = input("Enter your choice :")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid choice")

if __name__ == "__main__":
    main()