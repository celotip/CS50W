document.addEventListener('DOMContentLoaded', function() {
    view_count();
    viewpost(1);
    viewusers();
});

function view_count() {
    document.querySelector('#following').innerHTML = "";
    document.querySelector('#followers').innerHTML = "";
    fetch("profile/count")
    .then(response => response.json())
    .then(count => {
        document.querySelector('#followers').innerHTML = count["followers"];
        document.querySelector('#following').innerHTML = count["following"];
    })
};

function viewpost(page) {
    fetch(`profile/posts/page/${page}`)
    .then(response => response.json())
    .then(posts => {
        console.log(posts)
        document.querySelector('#posts').innerHTML = "";
        let fetchData = async postsArr => {
            for (let i = 0; i < postsArr.length; i++) {
                post_id = Number(postsArr[i]["id"])
                const response =  await fetch(`/posts/${post_id}`)
                const posts = await response.json()
                // Print posts
                console.log(posts);
                const post = document.createElement('div');
                post.className = 'post';
                post.setAttribute("id", `post/${posts['id']}`)
                document.querySelector('#posts').append(post);
                load_post(posts['id']);
                }
        }
        fetchData(posts);
        countpage("profile", page);
    })
}

function load_post(post_id) {
    fetch(`posts/${post_id}`)
    .then(response => response.json())
    .then(posts => {
        document.getElementById(`post/${post_id}`).innerHTML = "";
        const br = document.createElement('br');
        const time = document.createElement('div');
        time.setAttribute("style", "color:grey;");
        time.innerHTML = `${posts["timestamp"]}`;
        const user = document.createElement('div');
        user.innerHTML = `<b>${posts["user"]}</b>`;
        user.setAttribute("style", "font-size: 20px;");
        const likes = document.createElement('div');
        likes.innerHTML = `Likes: <span id="like/${posts['id']}"></span>`;
        const content_container = document.createElement('div');
        content_container.setAttribute("id", `content/${post_id}`)
        document.getElementById(`post/${post_id}`).append(user);
        document.getElementById(`post/${post_id}`).append(br);
        document.getElementById(`post/${post_id}`).append(content_container);
        document.getElementById(`post/${post_id}`).append(time);
        document.getElementById(`post/${post_id}`).append(likes);
        load_content(post_id);
        updatelike(post_id);
        });
}

function load_content(post_id) {
    fetch(`posts/${post_id}`)
    .then(response => response.json())
    .then(posts => {
        document.getElementById(`content/${post_id}`).innerHTML = "";
        const content = document.createElement('div');
        content.innerHTML = `${posts["content"]}`;
        const edit = document.createElement('button');
        edit.innerHTML = "Edit";
        edit.className = "edit";
        edit.addEventListener('click', function() {
            document.getElementById(`content/${post_id}`).innerHTML = "";
            const form = document.createElement('form');
            const editarea = document.createElement('textarea');
            editarea.innerHTML = content.innerHTML;
            const edit2 = document.createElement('button');
            edit2.innerHTML = "Edit post";
            edit2.className = "edit";
            form.append(editarea);
            form.append(edit2);
            document.getElementById(`content/${post_id}`).append(form);
            form.onsubmit = () => {
                fetch(`${post_id}/edit`, {
                    method: 'POST',
                    body: JSON.stringify({
                        content: editarea.value
                    })
                })
                .then(() => {
                    load_content(post_id);
                })
                return false;
            };
        });
        document.getElementById(`content/${post_id}`).append(content);
        document.getElementById(`content/${post_id}`).append(edit);
        });
}

function updatelike(post_id) {
    fetch(`${post_id}/likecount`)
    .then(response => response.json())
    .then(count => {
        document.getElementById(`like/${post_id}`).innerHTML = count["likes"];
    });
}

function viewusers() {
    fetch("profile/users")
    .then(response => response.json())
    .then(data => {
        console.log(data)
        document.querySelector('#users').innerHTML = "";
        for (let i = 0; i < data.length; i++) {
            const userdiv = document.createElement('div');
            userdiv.className = "user";
            const username = document.createElement('div');
            username.innerHTML = `${data[i]["username"]}`;
            username.className = "adv";
            userdiv.append(username);
            const follow = document.createElement('button');
            follow.innerHTML = "+ Follow";
            follow.className = "edit";
            follow.addEventListener('click', function() {
                fetch(`${Number(data[i]["id"])}/follow`, {
                    method: 'PUT',
                })
                .then(() => {
                    view_count();
                    viewusers();
                });
              });
            const unfollow = document.createElement('button');
            unfollow.innerHTML = "- Unfollow";
            unfollow.className = "edit";
            unfollow.addEventListener('click', function() {
                fetch(`${Number(data[i]["id"])}/unfollow`, {
                    method: 'PUT',
                })
                .then(() => {
                    view_count();
                    viewusers();
                });
              });
            fetch(`${Number(data[i]["id"])}/status`)
            .then(response => response.json())
            .then(status => {
                console.log(status)
                if (status["status"]) {
                    userdiv.append(unfollow);
                }
                else {
                    userdiv.append(follow);
                }
            })
            document.querySelector('#users').append(userdiv);
        }
    })
}

function countpage(type, page) {
    fetch(`/countpage/${type}`)
    .then(response => response.json())
    .then(data => {
        const pages = Number(data["pages"]);
        if (page === 1) {
            if (pages !== 1) {
                document.querySelector('#pagination').innerHTML = "";
                const next = document.createElement('li');
                next.className = "page-item";
                const nextlink = document.createElement('a');
                nextlink.href = "#"
                nextlink.className = "page-link";
                nextlink.addEventListener('click', function() {
                    viewpost(2);
                });
                nextlink.innerHTML = "Next";
                next.append(nextlink);
                document.querySelector('#pagination').append(next);
            }
        }
        else {
            document.querySelector('#pagination').innerHTML = "";
            const prev = document.createElement('li');
            prev.className = "page-item";
            const prevlink = document.createElement('a');
            prevlink.className = "page-link";
            prevlink.href = "#"
            const prevpage = page - 1;
            prevlink.addEventListener('click', function() {
                viewpost(prevpage);
            });
            prevlink.innerHTML = "Previous";
            prev.append(prevlink);
            document.querySelector('#pagination').append(prev);
            if (pages > page) {
                const next = document.createElement('li');
                next.className = "page-item";
                const nextlink = document.createElement('a');
                nextlink.className = "page-link";
                nextlink.href = "#"
                const nextpage = page + 1;
                nextlink.addEventListener('click', function() {
                    viewpost(nextpage);
                });
                nextlink.innerHTML = "Next";
                next.append(nextlink);
                document.querySelector('#pagination').append(next);
            }
        }
    });
}