import sqlite3

conn = sqlite3.connect('youtube_db.db')

cursor = conn.cursor()

cursor.execute(''' 
               CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
               )
               ''')


def list_all_videos():
    cursor.execute('''SELECT * FROM videos;''')
    for row in cursor.fetchall():
        print(row)

def update_video(video_id):
    new_name = input("Enter the new name of video :")
    new_time = input("Enter the new duration of video :")
    cursor.execute('''UPDATE videos WHERE id=?, name=?, time=?''', (video_id,new_name,new_time))
    conn.commit()

def add_video():
    name = input("Enter video name : ")
    time = input("Enter furation of video : ")
    cursor.execute('''INSERT INTO videos (name,time) VALUES(?, ?) ''', (name, time))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id=?",(video_id,))
    conn.commit()

def main():
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
                list_all_videos()
            case '2':
                add_video()
            case '3':
                list_all_videos()
                video_id = int(input("Enter the video id you want to update : "))
                update_video(video_id)
            case '4':
                list_all_videos()
                video_id = int(input("Enter the video id you want to delete : "))
                delete_video(video_id)
            case '5':
                break
            case _:
                print("Invalid choice")
    conn.close()


if __name__ == "__main__":
    main()