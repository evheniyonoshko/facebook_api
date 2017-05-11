import facebook
import schedule
import time
from datetime import datetime
import models
from config import token



def save_data(data):
    if not models.Posts.table_exists():
        models.Posts.create_table()
    else:
        try:
            post = models.Posts.get(post_id=data['post_id'])
            post.message = data['message']
            post.last_update = data['last_update']
            post.count_likes = data['count_likes']
            post.save()
        except:
            models.Posts.create(**data)
    print data

def main():
    graph = facebook.GraphAPI(token)
    # import ipdb; ipdb.set_trace()
    page = graph.get_object('wikrcom')
    posts = graph.get_connections("wikrcom", "posts")

    for post in posts['data']:
        likes = graph.get_connections(post['id'], "likes", limit=1000000)
        data = {
            'post_id': post['id'],
            'message': post['message'],
            'last_update': datetime.now(),
            'count_likes': len(likes['data']),
        }
        save_data(data)
    print '*** ALL DATA IS UPDATED ***'

if __name__ == '__main__':
    main()
    schedule.every(10).minutes.do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)
