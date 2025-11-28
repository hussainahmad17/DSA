// Callback version
function fetchDataCallback(callback) {
  setTimeout(() => {
    callback(null, "Data loaded using Callback");
  }, 1000);
}

// Usage
fetchDataCallback((err, data) => {
  if (err) console.error(err);
  else console.log(data);
});

 
//  conversion to proises

function fetchDataPromise() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve("Data loaded using Promise");
        }, 1000);
    })
}

fetchDataPromise().then(data => console.log(data)).catch(err => console.error(err));