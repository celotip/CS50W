document.addEventListener('DOMContentLoaded', function() {
    viewpost(1);
});

function viewpost(page) {
    fetch(`posts/following/page/${page}`)
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
                const br = document.createElement('br');
                const post = document.createElement('div');
                post.className = 'post';
                const time = document.createElement('div');
                time.setAttribute("style", "color:grey;");
                time.innerHTML = `${posts["timestamp"]}`;
                const user = document.createElement('div');
                user.innerHTML = `<b>${posts["user"]}</b>`;
                user.setAttribute("style", "font-size: 20px;");
                const content = document.createElement('div');
                content.innerHTML = `${posts["content"]}`;
                const likes = document.createElement('div');
                likes.innerHTML = `Likes: <span id="like/${posts['id']}"></span>`;
                const likebutt = document.createElement('div');
                likebutt.setAttribute("id", `button/${posts['id']}`);

                // Add post to DOM
                post.append(user);
                post.append(br);
                post.append(content);
                post.append(time);
                post.append(likes);
                post.append(likebutt);
                document.querySelector('#posts').append(post);
                likebutton(posts["id"]);
                updatelike(posts["id"]);
                }
        }
        fetchData(posts);
        countpage("following", page);
    })
}

function updatelike(post_id) {
    fetch(`${post_id}/likecount`)
    .then(response => response.json())
    .then(count => {
        document.getElementById(`like/${post_id}`).innerHTML = count["likes"];
    });
}

function likebutton(post_id) {
    const like = document.createElement('button');
    like.className = "likebutton";
    like.innerHTML = "♡"; 
    like.addEventListener('click', function() {
        fetch(`${post_id}/like`, {
            method: 'PUT',
        })
        .then(() => {
            updatelike(post_id);
            likebutton(post_id);
        });
    });
    const unlike = document.createElement('button');
    unlike.className = "likebutton";
    unlike.innerHTML = "♥";
    unlike.addEventListener('click', function() {
        fetch(`${post_id}/unlike`, {
            method: 'PUT',
        })
        .then(() => {
            updatelike(post_id);
            likebutton(post_id);
        });
    });
    fetch(`${post_id}/likestatus`)
    .then(response => response.json())
    .then(status => {
        console.log(status)
        if (status["status"]) {
            document.getElementById(`button/${post_id}`).innerHTML = "";
            document.getElementById(`button/${post_id}`).append(unlike);
        }
        else {
            document.getElementById(`button/${post_id}`).innerHTML = "";
            document.getElementById(`button/${post_id}`).append(like);
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