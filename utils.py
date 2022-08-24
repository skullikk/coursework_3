import json

def get_posts_all():
    with open('./data/posts.json', 'r', encoding='utf-8') as file_read_posts:
        posts = json.load(file_read_posts)
        return posts


def get_posts_by_user(user_name):
    result_posts = []
    result_user_name = []
    for post in get_posts_all():
        result_user_name.append(post['poster_name'])
        if user_name.lower() == post['poster_name'].lower():
            result_posts.append(post)
    if user_name not in result_user_name:
        raise ValueError
    return result_posts

def get_comments_by_post_id(post_id):
    with open('./data/comments.json', 'r', encoding='utf-8') as file_read_comments:
        comments = json.load(file_read_comments)
        result_comments = []
        result_post_id = []
        for comment in comments:
            result_post_id.append(comment['post_id'])
            if post_id == comment['post_id']:
                result_comments.append(comment)
        if post_id not in result_post_id:
            raise ValueError
        return result_comments

def search_for_posts(query):
    result_posts_search = []
    for post in get_posts_all():
        if query.lower() in post['content'].lower():
            result_posts_search.append(post)
    return result_posts_search

def get_post_by_pk(pk):
    for post in get_posts_all():
        if pk == post['pk']:
            return post

