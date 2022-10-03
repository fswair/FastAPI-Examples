from schemas import Post
def html_template(posts: dict|list[dict]):
    html_temps = ["<style>*{font-family:Montserrat, sans-serif;margin:15px; padding:5px;}</style>"]
    if type(posts) == list:
        for p in posts:
            post: Post = Post(*list(p.values()))
            html: str = f"""<h1>{post.post_title}</h1><h4>{post.post_created_date}</h4><h3>Author: {post.post_author}</h3><p>{post.post_description}</p>"""
            html_temps.append(html)
        return "<br><hr><br>".join(html_temps)
    post = Post(*posts)
    return f"""<h1>{post.post_title}</h1><h4>{post.post_created_date}</h4><h3>Author: {post.post_author}</h3><p>{post.post_description}</p>"""