
function add_product_to_cart(product_id) {
  data = {
    quantity: 10,
    product_id: product_id,
  };

    
    const myHeaders = new Headers();
    myHeaders.append('Content-Type', 'application/json');
    myHeaders.append('Content-Length', data.length);

    const myOptions = {
        method: 'POST',
        headers: myHeaders,
        mode: 'cors',
        cache: 'default',
        body: JSON.stringify({ data }),
    };
    const myRequest = new Request('/api/cart/', myOptions);

    fetch(myRequest).then((response) => {
        response.json()
    }).then((result) => {
        console.log(result)
    })
}


/*   header = {
    "Content-Type": "application/json",
    "Content-Length": data.length,
  };
  var requestOptions = {
    method: "POST",
    headers: header,
    body: JSON.stringify({ data }),
};

  fetch("/api/cart/", requestOptions)
    .then((response) => response.text())
    .then((result) => console.log(result))
    .catch((error) => console.log("error", error)); */