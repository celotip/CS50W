document.addEventListener("DOMContentLoaded", () => {
    if (document.getElementById(1)) {
        const link = document.getElementById(1);
        link.innerHTML = `<a href="options/6" class="btn btn-dark" >+</a>`;
        const info={
            "item":"Ayam rica-rica set",
            "price":25000
          }
        link.addEventListener('click', function() {
          localStorage.removeItem("kuah");
          localStorage.removeItem("drink");
          localStorage.setItem('counter', 1);
          add_set(info);
        });
    } 
    if (document.getElementById(2)) {
        const link = document.getElementById(2);
        link.innerHTML = `<a href="options/4" class="btn btn-dark" >+</a>`;
        const info={
            "item":"Opor ayam set",
            "price":23000
        }
          link.addEventListener('click', function() {
            localStorage.removeItem("kuah");
            localStorage.removeItem("drink");
            localStorage.setItem('counter', 1);
            add_set(info);
          });
    }

    if (document.getElementById(3)) {
      const link = document.getElementById(3);
      link.innerHTML = `<a href="options/4" class="btn btn-dark" >+</a>`;
      const info={
          "item":"Batagor",
          "price":15000
      }
        link.addEventListener('click', function() {
          localStorage.removeItem("kuah");
          localStorage.removeItem("drink");
          localStorage.setItem('counter', 1);
          add_set(info);
        });
  }

  if (document.getElementById(4)) {
    const link = document.getElementById(4);
    link.innerHTML = `<a href="options/4" class="btn btn-dark" >+</a>`;
    const info={
        "item":"Pisang Bakar",
        "price":8000
    }
      link.addEventListener('click', function() {
        localStorage.removeItem("kuah");
        localStorage.removeItem("drink");
        localStorage.setItem('counter', 1);
        add_set(info);
      });
}
})

function add_set(info){
  const set = [info];
  localStorage.setItem('set', JSON.stringify(set));
}

