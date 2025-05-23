import requests
#
from base import *

users = requests.get('https://jsonplaceholder.typicode.com/users').json()

lst_user = []
for user in users:
    name = user['name']
    username = user['username']
    email = user['email']
    phone = user['phone']
    address = f'Город: {user["address"]["city"]}, улица: {user["address"]["street"]}, кв-№: {user["address"]["suite"]}'
    save_users_data(name, username, email, phone, address)

posts = requests.get('https://jsonplaceholder.typicode.com/posts').json()

for post in posts:
    title = post['title']
    body = post['body']
    user_id = post['userId']
    save_posts_data(title, body, user_id)

comments = requests.get('https://jsonplaceholder.typicode.com/comments').json()

for comment in comments:
    postId = comment['postId']
    name = comment['name']
    email = comment['email']
    body = comment['body']
    save_comment_data(name, email, body, postId)

albums = requests.get('https://jsonplaceholder.typicode.com/albums').json()
for album in albums:
    userId = album['userId']
    title = album['title']
    save_albums_data(title, userId)
#



photos = requests.get('https://jsonplaceholder.typicode.com/photos').json()

for photo in photos:
    albumId = photo['albumId']
    title = photo['title']
    url = photo['url']
    thumbnailUrl = photo['thumbnailUrl']
    save_photos_data(title, url, thumbnailUrl, albumId)
#
#





